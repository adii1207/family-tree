Please read this before running the familyTree.

We are using familyData.txt to add the basic family tree.
User can add there queries in the userData.txt.
In the Node, we have used heightOfNode that can be used to find the relation between two persons i.e. if height is 1 then will be siblings or cousins(but not used in the code since it was not required).
We have added King Shan as 'King-Shan' and Queen Anga as 'Queen-Anga'. To make the parsing easy while using ' ' as delimiter. PLEASE KEEP THIS IN MIND WHILE ADDING CHILD TO QUEEN ANGA. Rather than adding it as ADD_CHILD Queen Anga XYZ PQR => ADD_CHILD Queen-Anga XYZ PQR
#Assumptions:

Mother can only add the child.
Marriage is done before having a baby(since linkage is done after marriage in the code).
To find Paternal/Maternal relation, it is necessary to have Grand-Parent !!!
By default we are only considering the cross-marriage culture for ease.
We are printing the results in left to right occurence in the tree.(We can simply sort the result, to print in chronological fashion)
#Templates to Add members in familyTree:

Add Child:

ADD_CHILD A B C A: Mother-Name (that is already in the familyTree) B: Child-Name (to be added as a new Node) C: Child-Gender

Add Spouse:

MAKE_COUPLE A B A: PersonA (that is already there in the familyTree) B: PersonB (the new node to be added as spouse in the familyTree)

#Template to Query for relationship:

GET_RELATIONSHIP A B A: PersonName (already in familyTree otherwise it will show PERSON_NOT_FOUND) B: It can take below parameter for now - 1. Paternal-Uncle 2. Maternal-Uncle 3. Paternal-Aunt 4. Maternal-Aunt 5. Sister-In-Law 6. Brother-In-Law 7. Son 8. Daughter 9. Siblings
