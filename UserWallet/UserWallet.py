# -*- coding:utf-8 -*-
"""
Description:
    UserWallet
"""


from bitcoin import *
from ecdsa import SigningKey, NIST256p

import binascii
import hashlib
import sys
import os

# ../sdk/
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sdk'))

from AntShares.Network.RemoteNode import RemoteNode

from AntShares.Core.TransactionOutput import TransactionOutput
from AntShares.Core.TransactionInput import TransactionInput
from AntShares.Core.Transaction import Transaction
from AntShares.Core.RegisterTransaction import RegisterTransaction
from AntShares.IO.MemoryStream import MemoryStream
from AntShares.IO.BinaryWriter import BinaryWriter

from AntShares.Wallets.Wallet import *
from AntShares.Helper import *

# Create Outputs
Outputs = [TransactionOutput(
            AssetId='f252a09a24591e8da31deec970871cc7678cb55023db049551e91f7bac28e27b',
            Value='19800.0',
            ScriptHash='9c17b4ee1441676e36d77a141dd77869d271381d')]

# outputs = [{'Asset': u'AntCoin',
#             'Value': u'100',
#             'Scripthash': u'9c17b4ee1441676e36d77a141dd77869d271381d'}]
#
# inputs, coins, outputs = selectInputs(getInputs(), outputs)
#
# Inputs = [TransactionInput(
#             prevHash=inputs[0][0].split('-')[0],
#             prevIndex=inputs[0][0].split('-')[1])]

Inputs = [TransactionInput(
            prevHash='d9c8be3046cbc22799887219a469c6d89bbc95e45aebdf1252e40cc3d670f81d',
            prevIndex=0)]

Issuer = '030fe41d11cc34a667cf1322ddc26ea4a8acad3b8eefa6f6c3f49c7673e4b33e4b'
Admin = '9c17b4ee1441676e36d77a141dd77869d271381d'
tx = RegisterTransaction(Inputs, Outputs, 0x60, '测试', -0.00000001, Issuer, Admin)

stream = MemoryStream()
writer = BinaryWriter(stream)
tx.serializeUnsigned(writer)
reg_tx = stream.toArray()

print repr(reg_tx)
print tx.getScriptHashesForVerifying()
print big_or_little(sha256(binascii.unhexlify(reg_tx)))

# Prikey = '7d989d02dff495cc1bbc35e891c153b98781e015a20ce276b86afc7856f85efa'
# Redeem_script = '21030fe41d11cc34a667cf1322ddc26ea4a8acad3b8eefa6f6c3f49c7673e4b33e4bac'
# from ecdsa import SigningKey, NIST256p
# sk = SigningKey.from_string(binascii.unhexlify(Prikey), curve=NIST256p, hashfunc=hashlib.sha256)
# signature = binascii.hexlify(sk.sign(binascii.unhexlify(reg_tx),hashfunc=hashlib.sha256))
# print reg_tx + '014140' + signature + '23' + Redeem_script