<script src="https://apis.google.com/js/api.js"></script>
<script>
  /**
   * Sample JavaScript code for forms.forms.batchUpdate
   * See instructions for running APIs Explorer code samples locally:
   * https://developers.google.com/explorer-help/code-samples#javascript
   */

  function authenticate() {
    return gapi.auth2.getAuthInstance()
        .signIn({scope: "https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/forms.body"})
        .then(function() { console.log("Sign-in successful"); },
              function(err) { console.error("Error signing in", err); });
  }
  function loadClient() {
    gapi.client.setApiKey("YOUR_API_KEY");
    return gapi.client.load("https://forms.googleapis.com/$discovery/rest?version=v1")
        .then(function() { console.log("GAPI client loaded for API"); },
              function(err) { console.error("Error loading GAPI client for API", err); });
  }
  // Make sure the client is loaded and sign-in is complete before calling this method.
  function execute() {
    return gapi.client.forms.forms.batchUpdate({
      "resource": {
        "requests": [
          {
            "createItem": {
              "item": {
                "title": "Fase Apertura",
                "description": "Durante la coordinación inicial se aboradaron todos los aspectos relevantes del curso, registrados en minuta",
                "questionItem": {
                  "question": {
                    "required": true,
                    "choiceQuestion": {
                      "type": "CHECKBOX",
                      "options": [
                        {
                          "value": "1"
                        },
                        {
                          "value": "2"
                        },
                        {
                          "value": "3"
                        },
                        {
                          "value": "4"
                        },
                        {
                          "value": "5"
                        },
                        {
                          "value": "6"
                        },
                        {
                          "value": "7"
                        }
                      ]
                    }
                  }
                }
              }
            }
          },
          {
            "createItem": {
              "item": {
                "description": "Se proporcionaron los contactos del personal de operaciones y canales de comunicación para soporte",
                "questionItem": {
                  "question": {
                    "required": true,
                    "choiceQuestion": {
                      "type": "CHECKBOX",
                      "options": [
                        {
                          "value": "1"
                        },
                        {
                          "value": "2"
                        },
                        {
                          "value": "3"
                        },
                        {
                          "value": "4"
                        },
                        {
                          "value": "5"
                        },
                        {
                          "value": "6"
                        },
                        {
                          "value": "7"
                        }
                      ]
                    }
                  }
                }
              }
            }
          },
          {
            "createItem": {
              "item": {
                "title": "Fase Ejecución",
                "description": "El equipo de soporte dio apoyo en la etapa de inscripción, cuando fue requerido",
                "questionItem": {
                  "question": {
                    "required": true,
                    "choiceQuestion": {
                      "type": "CHECKBOX",
                      "options": [
                        {
                          "value": "1"
                        },
                        {
                          "value": "2"
                        },
                        {
                          "value": "3"
                        },
                        {
                          "value": "4"
                        },
                        {
                          "value": "5"
                        },
                        {
                          "value": "6"
                        },
                        {
                          "value": "7"
                        }
                      ]
                    }
                  }
                }
              }
            }
          },
          {
            "createItem": {
              "item": {
                "description": "El equipo de soporte resolvió oportunamente problemas de acceso, cuando fue requerido",
                "questionItem": {
                  "question": {
                    "required": true,
                    "choiceQuestion": {
                      "type": "CHECKBOX",
                      "options": [
                        {
                          "value": "1"
                        },
                        {
                          "value": "2"
                        },
                        {
                          "value": "3"
                        },
                        {
                          "value": "4"
                        },
                        {
                          "value": "5"
                        },
                        {
                          "value": "6"
                        },
                        {
                          "value": "7"
                        }
                      ]
                    }
                  }
                }
              }
            }
          },
          {
            "createItem": {
              "item": {
                "description": "La relatoría tuvo una buena recepción por parte de los usuarios",
                "questionItem": {
                  "question": {
                    "required": true,
                    "choiceQuestion": {
                      "type": "CHECKBOX",
                      "options": [
                        {
                          "value": "1"
                        },
                        {
                          "value": "2"
                        },
                        {
                          "value": "3"
                        },
                        {
                          "value": "4"
                        },
                        {
                          "value": "5"
                        },
                        {
                          "value": "6"
                        },
                        {
                          "value": "7"
                        }
                      ]
                    }
                  }
                }
              }
            }
          },
          {
            "createItem": {
              "item": {
                "title": "Fase de Cierre",
                "description": "El informe, diplomas, registros de asistencia y demás, fueron enviados oportunamente ",
                "questionItem": {
                  "question": {
                    "required": true,
                    "choiceQuestion": {
                      "type": "CHECKBOX",
                      "options": [
                        {
                          "value": "1"
                        },
                        {
                          "value": "2"
                        },
                        {
                          "value": "3"
                        },
                        {
                          "value": "4"
                        },
                        {
                          "value": "5"
                        },
                        {
                          "value": "6"
                        },
                        {
                          "value": "7"
                        }
                      ]
                    }
                  }
                }
              }
            }
          },
          {
            "createItem": {
              "item": {
                "description": "La facturación se realizó dentro de los plazos y cumpliendo las formas acordadas",
                "questionItem": {
                  "question": {
                    "required": true,
                    "choiceQuestion": {
                      "type": "CHECKBOX",
                      "options": [
                        {
                          "value": "1"
                        },
                        {
                          "value": "2"
                        },
                        {
                          "value": "3"
                        },
                        {
                          "value": "4"
                        },
                        {
                          "value": "5"
                        },
                        {
                          "value": "6"
                        },
                        {
                          "value": "7"
                        }
                      ]
                    }
                  }
                }
              }
            }
          },
          {
            "createItem": {
              "item": {
                "title": "Post venta",
                "description": "¿Recomendaría realizar el curso a otros funcionarios de su institución?",
                "questionItem": {
                  "question": {
                    "required": true,
                    "choiceQuestion": {
                      "type": "CHECKBOX",
                      "options": [
                        {
                          "value": "1"
                        },
                        {
                          "value": "2"
                        }
                      ]
                    }
                  }
                }
              }
            }
          },
          {
            "createItem": {
              "item": {
                "description": "Sugerencia, reclamo o comentarios",
                "questionItem": {
                  "question": {
                    "required": false,
                    "textQuestion": {
                      "paragraph": false
                    }
                  }
                }
              }
            }
          }
        ]
      }
    })
        .then(function(response) {
                // Handle the results here (response.result has the parsed body).
                console.log("Response", response);
              },
              function(err) { console.error("Execute error", err); });
  }
  gapi.load("client:auth2", function() {
    gapi.auth2.init({client_id: "YOUR_CLIENT_ID"});
  });
</script>
<button onclick="authenticate().then(loadClient)">authorize and load</button>
<button onclick="execute()">execute</button>