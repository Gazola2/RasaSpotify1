## happy path 1 (C:\Users\YGOR~1.GAZ\AppData\Local\Temp\tmpmwprt_t5\8dde6a1f086f4aaa8f8da27b190d9c00_conversation_tests.md)
* greet: hello there!   <!-- predicted: goodbye: hello there! -->
    - utter_greet
* mood_great: amazing   <!-- predicted: goodbye: amazing -->
    - utter_happy   <!-- predicted: utter_greet -->


## happy path 2 (C:\Users\YGOR~1.GAZ\AppData\Local\Temp\tmpmwprt_t5\8dde6a1f086f4aaa8f8da27b190d9c00_conversation_tests.md)
* greet: hello there!   <!-- predicted: goodbye: hello there! -->
    - utter_greet
* mood_great: amazing   <!-- predicted: goodbye: amazing -->
    - utter_happy   <!-- predicted: utter_greet -->
* goodbye: bye-bye!   <!-- predicted: greet: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_greet -->


## sad path 1 (C:\Users\YGOR~1.GAZ\AppData\Local\Temp\tmpmwprt_t5\8dde6a1f086f4aaa8f8da27b190d9c00_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: goodbye: not good -->
    - utter_cheer_up   <!-- predicted: utter_greet -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes   <!-- predicted: goodbye: yes -->
    - utter_happy   <!-- predicted: utter_greet -->


## sad path 2 (C:\Users\YGOR~1.GAZ\AppData\Local\Temp\tmpmwprt_t5\8dde6a1f086f4aaa8f8da27b190d9c00_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: goodbye: not good -->
    - utter_cheer_up   <!-- predicted: utter_greet -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really   <!-- predicted: search_type: not really -->
    - utter_goodbye   <!-- predicted: utter_greet -->


## sad path 3 (C:\Users\YGOR~1.GAZ\AppData\Local\Temp\tmpmwprt_t5\8dde6a1f086f4aaa8f8da27b190d9c00_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible   <!-- predicted: goodbye: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_greet -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no   <!-- predicted: greet: no -->
    - utter_goodbye   <!-- predicted: utter_greet -->


## say goodbye (C:\Users\YGOR~1.GAZ\AppData\Local\Temp\tmpmwprt_t5\8dde6a1f086f4aaa8f8da27b190d9c00_conversation_tests.md)
* goodbye: bye-bye!   <!-- predicted: greet: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_greet -->


## bot challenge (C:\Users\YGOR~1.GAZ\AppData\Local\Temp\tmpmwprt_t5\8dde6a1f086f4aaa8f8da27b190d9c00_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: search_type: are you a bot? -->
    - utter_iamabot   <!-- predicted: utter_greet -->


