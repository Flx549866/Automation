#script to replace domain on email and print new email

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    #index @ starts at index 6  just for testing/learning purposes
    print(email.index("@" + old_domain))
    print("Your old email is:", email)
    #replace old domain with new one
    new_email = email[:index] + "@" + new_domain + ".com"
    print ("Your new email is:",new_email)
    return new_email
  return email

#calls function 
replace_domain("felix@gmail.com","gmail","hotmail")

