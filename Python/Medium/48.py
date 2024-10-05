class A:
    def method(self):  # Add 'self' as the first parameter
        print("Hello")

a = A()
a.method()  # This will now work correctly
