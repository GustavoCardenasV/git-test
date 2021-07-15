
def urlEncode(text):
     converted = ""
     normalized = list(text.strip())
     for i in range(len(normalized)):
          if normalized[i] == " ":
               normalized[i] = "%20"
          converted = converted + normalized[i]
     return converted


print(urlEncode("Lighthouse Labs"))
print(urlEncode(" Lighthouse Labs  "))
print(urlEncode("blue is greener than purple for sure"))

