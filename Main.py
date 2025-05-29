import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia(user_agent='Test (codecrusader07@gmail.com)', language='en')

test_a = str(input("Enter a topic to search: "))
page_py = wiki_wiki.page(test_a)

if page_py.exists():
    print("Page - Title: %s" % page_py.title)
    result = str(".".join(page_py.summary.split(".")[0:4]))+"."
    print("Page - Summary: %s" % result)
    choice = input("Do you want to save this summary? (y/n)")
    if choice.lower() == "y":
        filename = test_a.replace(" ","_") + ".txt"
        with open(filename,"w+") as f:
            f.write(f"Title: {page_py.title}\n\nSummary:\n{result}")
        print("Saved File!")    
else:
    print("Page not found!")
