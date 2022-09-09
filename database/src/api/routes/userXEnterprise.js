const route = require('express').Router();
const UserXEnterpriseService = require('./../../services/userXEnterprise');

route.get('/', UserXEnterpriseService.list);

route.post('/', UserXEnterpriseService.create);

route.patch('/:id', UserXEnterpriseService.update);

route.delete('/:id', UserXEnterpriseService.delete);


module.exports = route;