print('-----list start---------')
listTemp = ['xiaoming', 'xiaohong', 'xiaozhi']
listTemp.append('xiaozhang')
print(listTemp[2])
listTemp.insert(2, 'xiaowang')
print(listTemp[2])
listTemp.pop()
print(listTemp)

print('-----tuple start---------')
tupleTemp = (listTemp, 1, 2, 3)
print(tupleTemp[0])
listTemp.append("xiaofeng")
print(tupleTemp)

print('-----if else start---------')
if tupleTemp != None:
    print('tupleTemp is not None')
    print('if is not end')
else:
    print('tupleTemp is None')
if isinstance(tupleTemp[0], list):
    print('tupleTemp[0] is list')
    print(tupleTemp[0])

print('-----for in start---------')
for item in tupleTemp:
    print(item)

print('-----dict start---------')
dictTemp = {"key1": "value1", "key2": "value2"}
print(dictTemp)
print(dictTemp["key1"])
if "key2" in dictTemp:
    print(dictTemp["key2"])
    dictTemp.pop("key2")
print(dictTemp)
dictTemp["key3"] = "value3"
print(dictTemp)
for key, value in dictTemp.items():
    print('key:', key, 'value:', value)

print('-----set start---------')
setTemp = {1, 2, 3}
setTemp.add(4)
print(setTemp)

print('-----fun start---------')


def func_(x):
    print(x)


func_(23333)

print('-----list make test---------')
L = ['Hello', 'World', 18, 'Apple', None]
lowerList = [value.lower() for value in L if isinstance(value, str)]
print(lowerList)

print('-----@property test---------')


class Student(object):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            print("name is must a string")


student = Student()
student.name = "luchenwei"
print(student.name)
