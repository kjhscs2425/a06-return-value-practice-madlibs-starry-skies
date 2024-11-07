adjective0 = input("Give me an adjective: ")
noun0 = input("Give me a noun: ")
pluralnoun0 = input("Give me a plural noun: ")
personinroom0 = input("Give me a female name: ")
adjective1= input("Give me another adjective: ")
clothing0=input("Give me a type of clothing: ")
noun1 = input("Give me another noun: ")
city0 = input("Give me a city")
pluralnoun1 = input("Give me a plural noun: ")
adjective2= input("Give me another adjective: ")
adjective3= input("Give me an adjective ending in 'ier':")

if {noun0} == "a_" or "e_" or "i_" or "o_" or "u":
    an_or_a = "an"
else:
    an_or_a = "a"



story = f"There are many {adjective0} ways to choose " + an_or_a + f" {noun0} to read. First, you could ask for recommendations from your friends and {pluralnoun0}. Just don't ask Aunt {personinroom0} --- she only reads {adjective1} books with {clothing0} - ripping goddesses on the cover. If your friends and family are no help, try checking out the {noun1} Review in The {city0} Times. If the {pluralnoun1} featured there are too {adjective2} for your taste, try something a little {adjective3}"
print(story)

        