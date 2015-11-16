# -*- coding: cp936 -*-
import os
import math
import random
import Euclid
import fast_powmod
import prime_test
e = 65537
binary_bits = 1024#��ԼΪʮ���Ƶ�309λ������ʽ����ó�
binary_bits >>=1#�൱�ڳ���2��Ϊp��q��λ��
def produce_primes(binary_bits):
    """����ָ��λ���������"""
    while True:
        random.seed()#�ı����������
        odd = random.getrandbits(binary_bits)#����Ϊ2,����һ���������
        if len(bin(odd))-2 != binary_bits:
            continue
        if prime_test.fast_prime_test(odd) == False:#�ȿ����ж�һ���Ƿ�Ϊ����
            continue
        is_prime = prime_test.miller_rabin(odd)#miller_rabin�㷨���Բ���
        if is_prime == True:
            return odd
        elif is_prime == False:
            continue
def produce_p_q():
    """����������ͬ�Ĵ�����p��q"""
    p = produce_primes(binary_bits)
    len
    while True:
        q = produce_primes(binary_bits)
        if q != p:
            return(p,q)
def produce_CRT():
    (p,q) = produce_p_q()
    n = p*q
    Euler = (p-1)*(q-1) #ŷ������
    d = Euclid.extended_Euclid(e,Euler)#���eģEuler����Ԫd��e*d=1mod��Euler��
    dP = Euclid.extended_Euclid(e,p-1)
    dQ = Euclid.extended_Euclid(e,q-1)
    qInv = Euclid.extended_Euclid(q,p)
    return (p,q,n,d,dP,dQ,qInv)




