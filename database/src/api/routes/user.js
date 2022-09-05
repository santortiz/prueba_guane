const route = require('express').Router();
const UserService = require('../../services/user');

route.get(
    '/',
    async (req,res)=>{
        const payload = req.query;
        const response= await UserService.list(payload);
        res.status(response.status).json(
            response.data ? response.data: {detail: response.detail}
        );
    },
);

route.get('/:document', UserService.get);

route.post('/', UserService.create);

route.patch('/:document', UserService.update);

route.delete('/:document', UserService.delete);



module.exports = route;