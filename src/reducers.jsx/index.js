import auth from "./auth";
import * as notes from "./notes";
import * as auth from "./auth";


const ponyApp = combineReducers({
  notes, auth,
})

export {notes, auth}