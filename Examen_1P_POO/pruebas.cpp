class A
{
};

class B
{
public:
    B(int i = 0, const char *s = "", int j = 0) {}
    B &operator=(const B &b);
    B &operator=(const A &a);
    operator A() const;
};

B &B::operator=(const B &b)
{
}

B &B::operator=(const A &b)
{
}

B::operator A() const
{
}

int main(){
    B b1 = 0;
    A a3(b1);
    return 0;
}