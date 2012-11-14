#!/usr/bin/env python
# -*- coding: utf-8 -*
import twitterCommunication
import glue
import secret

twitterCom = twitterCommunication.twitterCommunication()
g=glue.glue(twitterCom)
g.main()

