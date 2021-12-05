# include <stdio.h>

void
main()
{
    int
tien, luachon, tiendu, soluong;

printf("Nhap so tien mua:");
scanf("%d", & tien);
printf(" Nhap lua chon mat hang can mua: ");
scanf("%d", & luachon);

switch(luachon)
{
    case
1:
{
    printf(" Lua chon: Tra xanh C2-");
if (tien < 9000)
{
    printf(" Khong du tien mua mat hang");
}
else
{
    soluong = tien / 9000;
tiendu = tien % 9000;
printf("soluong:%d - tien du:%d", soluong, tiendu);

}
}
}

case
2:
{

    printf(" Lua chon: Sting-");
if (tien < 11000)
{
    printf(" Khong du tien mua mat hang");
}
else
{
    soluong = tien / 11000;
tiendu = tien % 11000;
printf("soluong:%d - tien du:%d", soluong, tiendu);

}
}

case
3:
{
    printf(" Lua chon: Pepsi-");
if (tien < 10000)
{
    printf(" Khong du tien mua mat hang");
}
else
{
    soluong = tien / 10000;
tiendu = tien % 10000;
printf("soluong:%d - tien du:%d", soluong, tiendu);

}
}

case
4:
{
    printf(" Lua chon: Warrior-");
if (tien < 13000)
{
    printf(" Khong du tien mua mat hang");
}
else
{
    soluong = tien / 13000;
tiendu = tien % 13000;
printf("soluong:%d - tien du:%d", soluong, tiendu);

}
}

case
5:
{
    printf(" Lua chon: nuoc suoi-");
if (tien < 5000)
{

    printf(" Khong du tien mua mat hang");
}
else
{
    soluong = tien / 5000;
tiendu = tien % 5000;
printf("soluong:%d - tien du:%d", soluong, tiendu);

}
}

}