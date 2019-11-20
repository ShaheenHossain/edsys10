# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

import json

from eagle import models
from eagle.http import request

import eagle


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        user = request.env.user
        res = super(Http, self).session_info()
        res.update({
            "config_id": user.pos_config.id if user.pos_config else 1,
        })
        return res
