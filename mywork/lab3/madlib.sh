#!/bin/bash

clear
echo "Let's build a mad-lib!"

read -p "1. Please give me a noun: " NOUN1
read -p "2. Please give me a past-tense verb: " VERB1
read -p "3. Please give me an adjective: " ADJ1
read -p "4. Please give me a name: " NAME1
read -p "5. Please give me a place: " PLACE1
read -p "6. Please give me an adverb: " ADVERB1
read -p "7. Please give me an adjective: " ADJ2
read -p "8. Please give me an interjection: " INTJEC1

echo "Once upon a time, there was a $NOUN1."
echo "This $NOUN1 $VERB1 all across the land."
echo "The $NOUN1 was $ADJ1 and was named $NAME1."
echo "One day, $NAME1 went to $PLACE1 $ADVERB1."
echo "$NAME1 thought this new place was $ADJ2."
echo "What an incredible story, $INTJEC1!"
