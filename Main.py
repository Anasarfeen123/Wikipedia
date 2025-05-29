import wikipediaapi
import re
wiki_wiki = wikipediaapi.Wikipedia(user_agent='Test (codecrusader07@gmail.com)', language='en')

while True:
    choice_main = str(input("\nEnter a topic to search (or type '<exit>' to quit): ")).strip()
    if choice_main.lower() == "<exit>":
        print("exiting..")
        break
    else: 
        test_a = choice_main 
        page_py = wiki_wiki.page(test_a)

        if page_py.exists():
            print("Page - Title: %s" % page_py.title)
            result = str(".".join(page_py.summary.split(".")[0:4]))
            if not result.endswith("."):
                result += "."
            print("Page - Summary: %s" % result)
            choice = input("Do you want to save this summary? (y/n)").strip().lower()
            if choice == "y":
                filename = re.sub(r"[^\w\-_\.]", "_", test_a) + ".txt"
                with open(filename,"w+", encoding="utf-8") as f:
                    f.write(f"Title: {page_py.title}\n\nSummary:\n{result}")
                print("Saved File!")    
        else:
            print("Page not found!")
