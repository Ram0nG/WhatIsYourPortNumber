#This Program will ask for Network Device Port Number an also
#Patch Panel number to log into a file.

def main():
    #Create a variable to control the loop.
    another = "y"

#Open the PortandPatch.txt file in append mode.
PortandPatch = open('PortandPatch.txt', 'a')

# Add record to the file.
while another == 'y' or another == 'Y':
    #Get the PortandPatch record data.
    print('Enter the Port Number:')
    descr = input('Description: ')
    qty = int(input('How many Port do you enable: '))

    #Append the data to the file.
    PortandPatch.write(descr + '\n')
    PortandPatch.write(str(qty) '\n')

    #Determine whether the user wants to add
    #antoher record to the file.
    print('Do you want to add anther entry?')
    another = input('Y = yes, anything else = no: ')

    #close the file.
    PortandPatch.close()
    print('Data appended to PortandPatch.txt.')

# Call the main function.
main()
