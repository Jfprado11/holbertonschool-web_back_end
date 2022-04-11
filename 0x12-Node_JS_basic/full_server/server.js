import express from 'express';

import routes from './routes/index';

const port = 1245;
const app = express();

app.use('', routes());

app.listen(port);

export default app;
