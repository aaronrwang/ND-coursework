#!/usr/bin/env python3

from bst import BSTree
import ast

def print_help():
    print("Commands:")
    print("  (q)uit")
    print("  (hel)p")
    print("  (cle)ar")
    print("  (ins)ert <value>")
    print("  (con)tains <value>")
    print("  (ino)rder")
    print("  (len)gth")
    print("  (hei)ght")
    print("  (rem)ove <value>")
    print("  (wbf)s <list>--write to BFS list")
    print("  (pri)nt")
    print("-- Homework --")
    print("  (pre)order")
    print("  (pos)torder")
    print("  (bal)anced")
    print("  (inv)ert")
    print("  (pat)hs")
    print("  (rbf)s <list>--read from BFS list")
    print("  (val)idBst")
    print()

def main():
    bst = BSTree()
    print_help()

    while True:
        command_line = input("Enter command or (hel)p: ").strip().split()
        if not command_line:
            continue
        command = command_line[0].lower()
        
        # quit
        if command.startswith("q"):
            break
        # help
        elif command.startswith("hel"):
            print_help()
        # clear
        elif command.startswith("cle"):
            bst.clear()
            print("Cleared the BST.")
        # insert
        elif command.startswith("ins"):
            # Turn the rest of the command line into a single string
            arg_string = " ".join(command_line[1:])
            # Evaluate the string as a Python literal
            arg = ast.literal_eval(arg_string)
            bst.insert(arg)
            print(f"Inserted {arg} into the BST.")
            print(bst)
        # contains
        elif command.startswith("con"):
            arg_string = " ".join(command_line[1:])
            arg = ast.literal_eval(arg_string)
            print(arg in bst)
        # inorder
        elif command.startswith("ino"):
            print(bst.inorder())
        # len
        elif command.startswith("len"):
            print(len(bst))
        # height
        elif command.startswith("hei"):
            print(bst.height())
        # remove
        elif command.startswith("rem"):
            arg_string = " ".join(command_line[1:])
            arg = ast.literal_eval(arg_string)
            bst.remove(arg)
            print(f"Deleted {arg} from the BST.")
            print(bst)
        # write_bfs
        elif command.startswith("wbf"):
            print(bst.write_bfs())
        # print
        elif command.startswith("pri"):
            print(bst)

        #---- Homework Commands ----

        # preorder
        elif command.startswith("pre"):
            print(bst.preorder())
        # postorder
        elif command.startswith("pos"):
            print(bst.postorder())
        # is_balanced
        elif command.startswith("bal"):
            print(bst.is_balanced())
        # invert
        elif command.startswith("inv"):
            bst.invert()
            print(bst)
        # paths
        elif command.startswith("pat"):
            print(bst.paths())
        # read_bfs
        elif command.startswith("rbf"):
           arg_string = " ".join(command_line[1:])
           arg = ast.literal_eval(arg_string)
           bst.read_bfs(arg)
           print(bst)
        # is_valid_bst
        elif command.startswith("val"):
            print(bst.is_valid_bst())
            
        else:
            print("Invalid command")
            print_help()

if __name__ == "__main__":
    main()