const route = require('express').Router();
const EnterpriseService = require('../../services/enterprise');

route.get(
    '/',
    async (req,res)=>{
        const payload = req.query;
        const response= await EnterpriseService.list(payload);
        res.status(response.status).json(
            response.data ? response.data: {detail: response.detail}
        );
    },
);

route.get('/:id', EnterpriseService.get);

route.post('/', EnterpriseService.create);

route.patch('/:id', EnterpriseService.update);

route.delete('/:id', EnterpriseService.delete);



module.exports = route;