# def get_value(data: str, separator: str, position: int) -> str:
#   splitted_strings = data.split(separator) 
#   if 0 <= position < len(splitted_strings):
#       return splitted_strings[position]

#   else:
#     return ""
 
# toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
# separator = ','
# position= 8 
# result = get_value(toets_data, separator, position)
# print(result) 



# DEEL2

import re
text = "Geachte heer/mevrouw,Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. Ik ben de beste kandidaat voor deze functie omdat ik al jaren ervaring heb in deze branche en ik weet dat niemand anders mijn niveau van kennis en vaardigheden kan evenaren. Ik ben buitengewoon slim en in staat om snel nieuwe informatie te verwerken en te gebruiken om de beste beslissingen te nemen voor het bedrijf. Ik ben er zeker van dat ik binnen enkele weken op de hoogte zal zijn van alle zaken die spelen binnen uw bedrijf, en ik zal in staat zijn om snel resultaten te boeken en uw bedrijf naar de top te brengen. Mijn CV is overtuigend! Mijn referenties zijn heel positief over mij. Ik verdien daarom een plek in uw team.Ik kijk er naar uit om te horen wanneer ik op gesprek mag komen, zodat ik u persoonlijk kan overtuigen van mijn geschiktheid voor deze functie"
def get_sub(text):
  marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
  sub_sentences = marked_text.split("|") # split de text on marker "|"
  return sub_sentences



def get_ego_score(sub_sentences):
  ego_score = 0
  for sentence in sub_sentences: # repeat for every sentence in a list sentences
    sentence = sentence.strip() # remove leading and trailing spaces
    sentence = sentence.lower() # convert uppercase characters to lowercase
    if len(sentence) > 0:
      words = sentence.split(' ') # split sentence into words
      # first words of sentence equal to ik?
      if len(words) >= 2 and (words[0] in ('ik','mijn') or words[1] in ('ik','mijn')):
        ego_score += 1
  return ego_score

sub_sentences = get_sub(text) 
ego_score = get_ego_score(sub_sentences)

print(ego_score)