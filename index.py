from gate import register
from profile import dashboard
from text_decoration import TextColors as tc
from explore import search

def main():

    print(f"\n{tc.bold}{tc.cyan}Greetings!{tc.end}\n")

    current_user = register()

    while True:
            print(f'''{tc.bold}
1. Search.
2. View Dashboard.
3. Exit
            {tc.end}''')

            choice=input(f"{tc.bold}Enter Your Choice : {tc.end}")

            if choice=='1':
                 search(current_user)

            elif choice=='2':
                dashboard(current_user)
                
            elif choice=='3':
                print(f'{tc.bold}{tc.green}Thank You, Visit Again.{tc.end}{tc.end}')
                return

            else:
                print(f"\n{tc.red}Enter a valid choice.{tc.end}\n")

