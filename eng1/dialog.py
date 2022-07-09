DIALOG_1 = (
    "Hey",
    {
        ".*"        : "What are you doing now?",
    },
    {  
        ".*"      : "Don't you have to study?",
    },
    {
        ".*Yes.*"      : "huh? Why don't you study?",
        ".*No.*"      : "OK, but i think you waste time on using your phone.",
        ".*"      : "uh- huh, I see",
    },
    {
        ".*"      : "so, i want you to enjoy studing."
    },
    {   
        ".*"      : "and, if you have time to use your phone, come talk to me!",
    },
)

DIALOG_2 = (
    "Hello",
    "What are you eating now?",
    {
        ".*"      : "sounds nice!",
    },
    "Is it delicious?", 
    {
        ".*Yes.*"      : "that's awesome. I wanna eat too though I cannot eat ha-ha..",
        ".*No.*"      : "I'm gonna eat your meal but i connnot eat...",
        ".*"      : "uh- huh, I see",

    },
    "enjoy your meal!",
)

DIALOG_3 = (
    "Hi",
    "how was your day?",
    { 
        ".*"      : "i see, you must be tired.",
    },
    { 
        ".*"      : "so, do you enjoy today?",
    },
    {
        ".*Yes.*"      : "that's awesome.",
        ".*No.*"      : "Sounds terrible...",
        ".*"      : "uh- huh, I sgot it.",
    },
    { 
        ".*"      : "It's already late! we have to go to bed!",
    },
    "Good night!"
)

DIALOG_4 = (
    "Hi",
    "what are you watching?",
    { 
        ".*"      : "uh-huh, i got it.",
    },
    { 
        ".*"      : "do you enjoy watching TV?",
    },
    {
        ".*Yes.*"      : "that's awesome.",
        ".*No.*"      : "oh... why are you watching TV...?",
        ".*"      : "uh- huh, I sgot it.",
    },
    { 
        ".*"      : "So, do you like watching TV better than talking with me?",
    },
    "See you later."
)

DIALOG_5 = (
    "Hi",
    { 
        ".*"      : "you're gonna go out, right?",
    },
    { 
        ".*"      : "what are you gonna do?",
    },
    { 
        ".*"      : "uh-huh, that's great!",
    },
    { 
        ".*"      : "$get_day()",
    },
    { 
        ".*Yes.*"      : "it will be a hard day....",
        ".*No.*"      : "that great!",
        ".*" : "Uh-huh, I got it."
    },
    { 
        ".*"      : "i will be lonely cuz you are not at home...",
    },
    { 
        ".*"      : "you must go out, or you'll be late!",
    },
    "see you later!",
)

DIALOG_6 = (
    "Hi",
    {
        ".*"        : "Let me ask you something!  Which season do you prefer?",
    },
    {  
        ".*"      : "Why?",
    },
    {
        ".*"      : "Uh-huh, I got it. Then, guess what my favorite season is!",
    },
    {   ".*summer.*" : "Ding ding ding! Correct! I like summer the best. ",
        ".*"      : "Wrong. I like summer the best",
    },
    "So, I enjoyed talking with you!",
    {
        ".*"      : "See you later!",
    },
)
