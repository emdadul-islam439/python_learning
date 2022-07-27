#define a set

st = set()
print(st)
print(type(st))

#adding single elements
st.add(5)
print(st)
print(len(st))


#can add multiple elements by 'updating' the set
st.update([1,2,4,3])
print(st)
print(len(st))


##can't 'directly' add multiple items
# st.add([1,2,4,3])
# print(st)
# print(len(st))

#adding another set directly
#st.add({1,6,7}) #won't work
st.update({1,6,7})
print(st)

#union-intersection
st.union({9,10}) #st won't be updated
print(st)
st2 = st.union({9,10})
print(st2)

st2 = st.intersection({6,7,8,9})
print(st2)


#copying without reference
st2=st.copy()
print(st2)


#different operations
print(len(st2))
print(max(st2))
print(min(st))
print(st.isdisjoint(st2)) #is nothing is common
print(st)
st.remove(2)
print(st)