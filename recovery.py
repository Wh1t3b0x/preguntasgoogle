import json
import boto3
import os
import time
import shutil
from monday import MondayClient
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.discovery import build
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

def get_secret():

    secret_name = "Monday_API"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    return json.loads(get_secret_value_response['SecretString'])
    
SCOPES = ["https://www.googleapis.com/auth/forms.body","https://www.googleapis.com/auth/drive"]
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
API_KEY = get_secret()['monday_api']
COLUMNA = "enlace8"
BOARD = "3549229417"

creds=None
session = boto3.session.Session()
                                
client = session.client('s3')
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credential.json', SCOPES)
        creds = flow.run_local_server(port=0)
    shutil.copyfile('token.json','/tmp/token.json')
    # Save the credentials for the next run
    with open('/tmp/token.json', 'w') as token:
        token.write(creds.to_json())
    
    
form_service = build('forms', 'v1', credentials=creds,discoveryServiceUrl=DISCOVERY_DOC,static_discovery=False)

def syncchallenge(event: dict):
    try:
      event_body = json.loads(event['body'])
      challenge = {'challenge' : event_body['challenge']}
      return challenge
    except Exception as e:
      return
    

def lambda_handler(event, context):
    print(event)
    
    if (challenge:= syncchallenge(event)):
        return{
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": json.dumps(challenge),
        "headers": {
        "content-type": "application/json"
        }
        }
    
    evento = json.loads(event["body"])['event']
    
    time.sleep(5)
    
    mon=MondayClient(API_KEY)
    fila=mon.items.fetch_items_by_id(evento['pulseId'])
    curso=None
    
    for elemento in fila['data']['items'][0]['column_values']:
        if elemento['id']=='texto14':
            curso=elemento['text']
            break
    if not curso:
        print('No existe Curso')
        exit()
        
    # Crear el objeto de servicio de la API de Google Drive
    service = build('drive', 'v3', credentials=creds)
    
    
    id_PADRE='1E-nU0ZiWrxqfUYSSkADFPst6hYGQQz8c'
    # Especificar el nombre de la carpeta que se va a buscar
    nombre_carpeta = evento['pulseName']
    
    # Crear la query para buscar la carpeta por su nombre
    query = "mimeType='application/vnd.google-apps.folder' and trashed=false and name='{}'".format(nombre_carpeta)
    
    # Realizar la búsqueda de la carpeta
    resultados = service.files().list(q=query, fields='files(id, name)').execute()
    
    # Obtener el ID y nombre de la carpeta encontrada, si hay resultados
    if resultados.get('files', []):
        carpeta = resultados['files'][0]
        id_carpeta = carpeta['id']
        nombre_carpeta = carpeta['name']
        print("La carpeta '{}' fue encontrada con ID: {}".format(nombre_carpeta, id_carpeta))
    else:
        print("No se encontró la carpeta '{}'".format(nombre_carpeta))
        exit()
    
    
    
    # Especificar el nombre del archivo que se va a buscar
    nombre_archivo='Encuesta Encargado-'+curso
    
    # Crear la query para buscar el archivo por su nombre
    query = "trashed=false and name='{}'".format(nombre_archivo)
    
    # Realizar la búsqueda del archivo
    resultados = service.files().list(q=query, fields='files(id, name)').execute()
    
    # Obtener el ID y nombre del archivo encontrado, si hay resultados
    if resultados.get('files', []):
        archivo = resultados['files'][0]
        id_archivo = archivo['id']
        nombre_archivo = archivo['name']
        print("El archivo '{}' fue encontrado con ID: {}".format(nombre_archivo, id_archivo))
        exit()
    else:
        print("No se encontró el archivo '{}'".format(nombre_archivo))
    
    
    
    
    NEW_FORM = {
        "info": {
            "title": f"{nombre_archivo}",
            "documentTitle": f"{nombre_archivo}"
        }
    }


    NEW_QUESTION_TWO = {
        "requests": [{
            "createItem": {
                "item": {
                    "title": "Rut",
                    "description": "Ingrese su rut en formato 'xx.xxx.xxx-x' o 'xxxxxxxx-x' Siempre ingresando su guion",
                    "questionItem": {
                        "question": {
                            "required": True,

                              "textQuestion": {                    
                                "paragraph": True
                              }

                        }
                    },
                },



                "location": {
                    "index": 0
                }
            },

        }]
    }

    NEW_QUESTION_THREE = {
        "requests": [{
            "createItem": {
                "item": {
                    "title": "Apellidos",
                    "questionItem": {
                        "question": {
                            "required": True,
                              "textQuestion": {                    
                                "paragraph": True
                              }
                        }
                    },
                },

                "location": {
                    "index": 0
                }
            },

        }]
    }

    NEW_QUESTION_FOUR = {
        "requests": [{
            "createItem": {
                "item": {
                    "title": "Nombres",
                    "questionItem": {
                        "question": {
                            "required": True,
                              "textQuestion": {                    
                                "paragraph": True
                              }
                        }
                        }
                    },
                "location": {
                    "index": 0
                }
            },

        }]
    }

    IMAGE = {"requests":[{"createItem":{"item":{"imageItem":{"image":{"sourceUri":"https://imagenes-correo-boleta.s3.amazonaws.com/fondo.png"}}},"location":{"index":0}}}]}

    
    result = form_service.forms().create(body=NEW_FORM).execute()
    #Adds the question to the form
    #form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION_TWO).execute()
    #form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION_THREE).execute()
    #form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION_FOUR).execute()
    privacy_settings = {
    "settings": {
        "access": "ANYONE_WITH_LINK",
        }
    }

    # Solicitud para actualizar la configuración de privacidad del formulario
    #.forms().batchUpdate(formId=result["formId"], body=privacy_settings).execute()
    
    form_service.forms().batchUpdate(formId=result["formId"], body=IMAGE).execute()
    file = service.files().get(fileId=result["formId"], fields='parents').execute()
    previous_parents = ",".join(file.get('parents'))
    # Move the file to the new folder
    file = service.files().update(fileId=result["formId"], addParents=id_carpeta,
                                        removeParents=previous_parents,
                                        fields='id, parents').execute()
                                        
                                        
                        
    print(result['responderUri'])
    
    urlForm=result['responderUri']+'?usp=sf_link'
    correo=None
    #Enviamos el correo
    for elemento in fila['data']['items'][0]['column_values']:
        if elemento['id']=='dup__of_telefono_encargado':
            correo=elemento['text']
            break
    if not correo:
        print('No se puede enviar correo')
        exit()
        
    new_permission = {
        "emailAddress": correo,
        "role": 'commenter',
        "type": "user"
    }
    
    #service.permissions().create(fileId=result["formId"], body=new_permission).execute()    
    # Define these once; use them twice!
    strFrom = 'huellascapacitaciones@gmail.com'
    strTo = correo
    
    
    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = f'Encuesta Curso-{curso}'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'
    
    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    
    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)
    
    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText(f'''<p>Adjunto link de encuesta : {urlForm}</p>''', 'html')
    msgAlternative.attach(msgText)
    
    # Send the email (this example assumes SMTP authentication is required)
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.ehlo()
    smtp.login('huellascapacitaciones@gmail.com', "bakhvmguujfkjjmk")
    smtp.sendmail(strFrom, [strTo], msgRoot.as_string())
    smtp.quit() 
    return{
    
    "body": json.dumps(event),

    
    }