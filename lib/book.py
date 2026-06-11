
class Book:
    def __init__(self,title : str, page_count):
        self.title = title
        self.page_count = page_count

        
        
        if self.title == "":
            print ("Enter Title")
        else:
            title = str(input("Enter Title"))
        
        if self.page_count == int:
            page_count = int(input("Ensure it is an integer"))
            return self.page_count
        else:
            print("page_count must be an integer")
        
    def turn_page(self):
        if self.page_count == 0:
            print("You Need to study") 
        self.page_count += 1
        print("Flipping the page...wow, you read fast!")


        

    
    
        