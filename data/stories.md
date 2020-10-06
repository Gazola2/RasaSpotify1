## happy path
* greet
    - utter_greet
    - utter_explain

## start
* start
    - utter_greet
    - utter_explain

## full_album
* start
    - utter_greet
    - utter_explain
    - slot{"tipo":"artista"}
* search_tipo{"tipo":"artista"}
    - slot{"tipo":"artista"}
    - search_form
    - form{"name":"search_form"}
    - slot{"requested_slot":"artista"}
* artista
    - search_form
    - form{"name":null}
    - slot{"artista":"drake"}
* search_tipo{"tipo":"album","album":"3TVXtAsR1Inumwj472S9r4"}
    - search_form
    - form{"name":"search_form"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
    - utter_finish
* goodbye
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_goodbye

## full album - goodbye
* start
    - utter_greet
    - utter_explain
    - slot{"tipo":"artista"}
* search_tipo{"tipo":"artista"}
    - slot{"tipo":"artista"}
    - search_form
    - form{"name":"search_form"}
    - slot{"requested_slot":"artista"}
* artista
    - search_form
    - form{"name":"search_form"}
    - slot{"artista":"drake"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
* search_tipo{"tipo":"album","album":"3TVXtAsR1Inumwj472S9r4"}
    - search_form
    - form{"name":"search_form"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
    - utter_finish

## search_artists 2 vezes
* start
    - utter_greet
    - utter_explain
    - slot{"tipo":"artista"}
* search_tipo{"tipo":"artista"}
    - slot{"tipo":"artista"}
    - search_form
    - form{"name":"search_form"}
    - slot{"requested_slot":"artista"}
* artista
    - search_form
    - form{"name":null}
    - slot{"artista":"drake"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
* search_tipo{"tipo":"album","album":"3TVXtAsR1Inumwj472S9r4"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
    - slot{"tipo":"album"}
    - search_form
    - form{"name":"search_form"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
    - utter_finish
    - slot{"requested_slot":"artista"}
* artista
    - search_form
    - form{"name":null}
    - slot{"artista":"twice"}
    - slot{"album":"7n2Ycct7Beij7Dj7meI4X0"}
* search_tipo{"tipo":"album","album":"7n2Ycct7Beij7Dj7meI4X0"}
    - slot{"album":"7n2Ycct7Beij7Dj7meI4X0"}
    - slot{"tipo":"album"}
    - search_form
    - form{"name":"search_form"}
    - slot{"album":"7n2Ycct7Beij7Dj7meI4X0"}
    - utter_finish
* goodbye
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_goodbye

## full_album + greet
* greet
    - utter_greet
    - utter_explain
    - slot{"tipo":"artista"}
* search_tipo{"tipo":"artista"}
    - slot{"tipo":"artista"}
    - search_form
    - form{"name":"search_form"}
    - slot{"requested_slot":"artista"}
* artista
    - search_form
    - form{"name":null}
    - slot{"artista":"drake"}
* search_tipo{"tipo":"album","album":"3TVXtAsR1Inumwj472S9r4"}
    - search_form
    - form{"name":"search_form"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
    - utter_finish
* goodbye
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_goodbye

## full album - goodbye + greet
* greet
    - utter_greet
    - utter_explain
    - slot{"tipo":"artista"}
* search_tipo{"tipo":"artista"}
    - slot{"tipo":"artista"}
    - search_form
    - form{"name":"search_form"}
    - slot{"requested_slot":"artista"}
* artista
    - search_form
    - form{"name":"search_form"}
    - slot{"artista":"drake"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
* search_tipo{"tipo":"album","album":"3TVXtAsR1Inumwj472S9r4"}
    - search_form
    - form{"name":"search_form"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
    - utter_finish

## search_artists 2 vezes + greet
* greet
    - utter_greet
    - utter_explain
    - slot{"tipo":"artista"}
* search_tipo{"tipo":"artista"}
    - slot{"tipo":"artista"}
    - search_form
    - form{"name":"search_form"}
    - slot{"requested_slot":"artista"}
* artista
    - search_form
    - form{"name":null}
    - slot{"artista":"drake"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
* search_tipo{"tipo":"album","album":"3TVXtAsR1Inumwj472S9r4"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
    - slot{"tipo":"album"}
    - search_form
    - form{"name":"search_form"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
    - utter_finish
    - slot{"requested_slot":"artista"}
* artista
    - search_form
    - form{"name":null}
    - slot{"artista":"twice"}
    - slot{"album":"7n2Ycct7Beij7Dj7meI4X0"}
* search_tipo{"tipo":"album","album":"7n2Ycct7Beij7Dj7meI4X0"}
    - slot{"album":"7n2Ycct7Beij7Dj7meI4X0"}
    - slot{"tipo":"album"}
    - search_form
    - form{"name":"search_form"}
    - slot{"album":"7n2Ycct7Beij7Dj7meI4X0"}
    - utter_finish
* goodbye
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_goodbye

## search_artists 2 vezes + greet + interrupt
* greet
    - utter_greet
    - utter_explain
    - slot{"tipo":"artista"}
* search_tipo{"tipo":"artista"}
    - slot{"tipo":"artista"}
    - search_form
    - form{"name":"search_form"}
    - slot{"requested_slot":"artista"}
* goodbye
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_goodbye

## search_artists 2 vezes + greet + interrupt
* greet
    - utter_greet
    - utter_explain
    - slot{"tipo":"artista"}
* search_tipo{"tipo":"artista"}
    - slot{"tipo":"artista"}
    - search_form
    - form{"name":"search_form"}
    - slot{"requested_slot":"artista"}
* artista
    - search_form
    - form{"name":null}
    - slot{"artista":"drake"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
* search_tipo{"tipo":"album","album":"3TVXtAsR1Inumwj472S9r4"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
    - slot{"tipo":"album"}
    - search_form
    - form{"name":"search_form"}
    - slot{"album":"3TVXtAsR1Inumwj472S9r4"}
    - utter_finish
    - slot{"requested_slot":"artista"}
* goodbye
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_goodbye

## fallback
* start
    - utter_greet
    - utter_explain
* out_of_scope
    - action_my_fallback
* goodbye
    - utter_goodbye

## greet+goodbye
* start
    - utter_greet
    - utter_explain
* goodbye
    - utter_goodbye

## start
* start
    - utter_greet
    - utter_explain

## Menu
* ajuda
    - utter_ajuda

## ajuda

* start
    - utter_greet
    - utter_explain
* ajuda
    - utter_ajuda
* goodbye
    - utter_goodbye

## forms with help

* start
    - utter_greet
    - utter_explain
    - slot{"tipo":"artista"}
* search_tipo{"tipo":"artista"}
    - slot{"tipo":"artista"}
    - search_form
    - form{"name":"search_form"}
    - slot{"requested_slot":"artista"}
* ajuda
    - utter_ajuda
* artista
    - search_form
    - form{"name":null}
    - slot{"artista":"drake"}
* goodbye
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_goodbye

## New Story

* start
    - utter_greet
    - utter_explain
    - slot{"tipo":"artista"}
* search_tipo{"tipo":"artista"}
    - slot{"tipo":"artista"}
    - search_form
    - form{"name":"search_form"}
    - slot{"requested_slot":"artista"}
* goodbye
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_goodbye