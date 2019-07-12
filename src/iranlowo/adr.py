#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pkg_resources
from argparse import Namespace
from onmt.translate.translator import build_translator
from onmt.utils.parse import ArgumentParser


def diacritize_text(undiacritized_text, verbose=False):
    # manually construct the options so we don't have to pass them in.
    opt = Namespace()
    opt.alpha = 0.0
    opt.attn_debug = False
    opt.avg_raw_probs = False
    opt.batch_size = 30
    opt.beam_size = 5
    opt.beta = -0.0
    opt.block_ngram_repeat = 0
    opt.config = None
    opt.coverage_penalty = 'none'
    opt.data_type = 'text'
    opt.dump_beam = ''
    opt.dynamic_dict = False
    opt.fp32 = False
    opt.gpu = -1
    opt.ignore_when_blocking = []
    opt.image_channel_size = 3
    opt.length_penalty = 'none'
    opt.log_file = ''
    opt.log_file_level = '0'
    opt.max_length = 100
    opt.max_sent_length = None
    opt.min_length = 0
    opt.n_best = 1
    opt.output = 'pred.txt'
    opt.phrase_table = ''
    opt.random_sampling_temp = 1.0
    opt.random_sampling_topk = 1
    opt.ratio = -0.0
    opt.replace_unk = True
    opt.report_bleu = False
    opt.report_rouge = False
    opt.report_time = False
    opt.sample_rate = 16000
    opt.save_config = None
    opt.seed = 829
    opt.shard_size = 10000
    opt.share_vocab = False
    opt.src = 'one_phrase.txt'
    opt.src_dir = ''
    opt.stepwise_penalty = False
    opt.tgt = None
    opt.verbose = verbose
    opt.window = 'hamming'
    opt.window_size = 0.02
    opt.window_stride = 0.01

    model_path = 'models/yo_adr_soft_attention_release.pt'
    opt.models = [pkg_resources.resource_filename(__name__, model_path)]

    # do work
    ArgumentParser.validate_translate_opts(opt)
    translator = build_translator(opt, report_score=True)

    # src_shard = ["awon okunrin nse ise agbara bi ise ode".encode('ascii')]
    src_shard = [undiacritized_text.encode('ascii')]
    tgt_shard = None

    score, prediction = translator.translate(
        src=src_shard,
        tgt=tgt_shard,
        src_dir=opt.src_dir,
        batch_size=opt.batch_size,
        attn_debug=opt.attn_debug
    )
    return prediction[0][0]

