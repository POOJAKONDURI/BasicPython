
'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python p
    rogram to 

'''


def noteschange(change, notes):
    """
        description:
            This prog is to give change of particular ip amount which is minunm notes and rs notes in lst
        parameters:
            change : input rs amount,
            notes: lst of notes to give it as change
        return:
            Returns minimum number of notes and rs notes
    """
    if change == 0:
        return 0, []
    

    for note in reversed(notes):
        if change >= note:
            remaining_Change = change - note
            count, note_list = noteschange(remaining_Change,notes)
            return count + 1,[note] + note_list
    
def main():
    change = 650
    notes  =  [1,2,10,20,50,100,500,1000]
    mincnt, lst = noteschange(change, notes)
    print(f"minimum number of notes givn as change:{mincnt}")
    print(f"notes given as change {lst}")


if __name__ == "__main__":
    main()

          




                
           