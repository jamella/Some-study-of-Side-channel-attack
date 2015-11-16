#make by liujian,2015.07.16
# -*- coding: cp936 -*-
from product_crt import *
import sha
(p,q,N,D,dP,dQ,qInv)=produce_CRT()  #����CRT-RSA��Կ
print "***********************�����������Կ***********************"
print "˽Կ����p:",hex(p)[2:-1]
print "˽Կ����q:",hex(q)[2:-1]
print "˽ԿD:",hex(D)[2:-1]
print "��Կ����N",hex(N)[2:-1]
print "N���ȣ�",len(bin(N))-2,   "\D:����",len(bin(D))-2
print "**********************************************************"
sha1_OID="3021300906052b0e03021a05000414" #���� PKCS#1������EM�Ĳ���
#����ģ�����㣬�൱��pow��base,exp,n��
def fast_pow(base,exp,n):
    result=1
    while(exp):
        if exp&1:
            result=(result*base)%n
        exp=exp>>1
        base=(base*base)%n
    return result
#�����ģ�����㣬��ѡ��ע������:�����ڵ�4��expδ��λ
def fast_pow_F(base,exp,n):
    result=1
    i=1
    while(exp):
        i=i+1
        if exp&1:
            result=(result*base)%n
        else:
            pass
        if i==4:
           # exp=exp>>1
           base=((base)*base)%n     
        else:
            exp=exp>>1
            base=((base)*base)%n        
    return result
#CRT-RSAǩ�����ο���PKCS #1 V2.1��5.2.1 RSAP1
def sign(m,P,Q,Dp,Dq,Qinv):    
    s1=pow(m,Dp,P)
    s2=pow(m,Dq,Q)
    h=((s1-s2)*Qinv)%P
    C=s2+Q*h
    return C
#ѡ��ע��������㣬s1��s2������
def sign_F(m,P,Q,Dp,Dq,Qinv):   
    s1=fast_pow_F(m,Dp,P)
    s2=fast_pow(m,Dq,Q)
    h=((s1-s2)*Qinv)%P
    C1=s2+Q*h
    return C1
#���Լ�����㣬ŷ������㷨
#d=gcd(m,n)=>d|m,d|n,m=q1*n+r1
def gcd(m,n):
    while n:
        m,n=n,m%n
    return m
#M - M' = (((Mq - Mp)*K) mod q)*p - (((M'q - Mp)*K) mod q)*p = (x1-x2)*p
#��Gcd( M-M', n ) = Gcd( (x1-x2)*q, p*q ) = q,�����
def DFA_CRT_RSA(C,C1):
    q=gcd(C-C1,N)    
    return q    
def main():
    #��Ϣ����EM = 0x00 || 0x01 || PS || 0x00 || T,T=OID+H,��PKCS #1 V2.1��
    h=sha.new(raw_input("�����ǩ������:")).hexdigest()
    EM=int("0001ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"+"00"+sha1_OID+h,16)
    C=sign(EM,p,q,dP,dQ,qInv)
    C1=sign_F(EM,p,q,dP,dQ,qInv)
    q_F=DFA_CRT_RSA(C,C1)
    p_F=N/q_F
    q_F=hex(q_F)[2:-1]
    p_F=hex(p_F)[2:-1]
    print "��ȷǩ�������",hex(C)[2:-1],"\n����ǩ�����:",hex(C1)[2:-1]
    print "��ǩ��������",hex(fast_pow(C,65537,N))[2:-1]
    print "���������:\n",'p:',p_F,'\n','q:',q_F
    print "**********************************************************"
if __name__=="__main__":
    main()
    re=raw_input("�޸�ǩ�����ݰ�y����һ�Σ�")
    if re =="y":
                 
                main()
                re=raw_input("�޸�ǩ�����ݰ�y����һ�Σ�")
    else:
                pass
        

    
