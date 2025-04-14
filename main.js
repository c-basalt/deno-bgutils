import jsdom from "https://esm.sh/v135/jsdom";
localStorage.clear();
global = window = globalThis;
delete window.Deno;

const dom = new jsdom.JSDOM();
Object.assign(globalThis, {
    window: dom.window,
    document: dom.window.document
});
delete window.jsdom;


const bgConfig = {
    fetch,
    globalObj: globalThis,
    identifier: visitorData,
    requestKey: 'O43z0dpjhgX20SCx4KAo',
};


const bgChallenge = await BG.Challenge.create(bgConfig);
if (!bgChallenge) throw new Error('Could not get challenge');


const interpreterJavascript = bgChallenge.interpreterJavascript.privateDoNotAccessOrElseSafeScriptWrappedValue;
if (!interpreterJavascript) throw new Error('Could not load VM');
eval(interpreterJavascript);


const poTokenResult = await BG.PoToken.generate({
    program: bgChallenge.program,
    globalName: bgChallenge.globalName,
    bgConfig
});
const placeholderPoToken = BG.PoToken.generateColdStartToken(visitorData);

console.info(JSON.stringify({
    visitorData,
    placeholderPoToken,
    poToken: poTokenResult.poToken,
    integrityTokenData: poTokenResult.integrityTokenData
}, null, 2));