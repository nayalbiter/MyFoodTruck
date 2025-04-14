
function loadGoogleMapsAPI(config) {
    const p = "The Google Maps JavaScript API";
    const c = "google";
    const l = "importLibrary";
    const q = "__ib__";
    const m = document;
    const b = window;

    b[c] = b[c] || {};
    const d = b[c].maps = b[c].maps || {};

    const r = new Set();
    const e = new URLSearchParams();

    let h; // Promise holder

    function u() {
        if (h) return h;

        h = new Promise(async (resolve, reject) => {
            const a = m.createElement("script");
            e.set("libraries", [...r] + ""); // collect libraries as comma-separated string

            for (const k in config) {
                const paramKey = k.replace(/[A-Z]/g, t => "_" + t.toLowerCase());
                e.set(paramKey, config[k]);
            }

            e.set("callback", `${c}.maps.${q}`);
            a.src = `https://maps.${c}apis.com/maps/api/js?` + e;
            a.nonce = m.querySelector("script[nonce]")?.nonce || "";

            d[q] = resolve;
            a.onerror = () => {
                h = null;
                reject(new Error(`${p} could not load.`));
            };

            m.head.appendChild(a);
        });

        return h;
    }

    if (d[l]) {
        console.warn(`${p} only loads once. Ignoring:`, config);
    } else {
        d[l] = (f, ...n) => {
            r.add(f);
            return u().then(() => d[l](f, ...n));
        };
    }
}

loadGoogleMapsAPI({
    key: "AIzaSyAOacv_xm8875Kv69dQpWanhvZfzz7dgXA",
    v: "weekly" // version of the API to use
});


/* this code uses  Immediately Invoked Function Expression (IIFE).
<script>
    (g => { var h, a, k, p = "The Google Maps JavaScript API", c = "google", l = "importLibrary", q = "__ib__", m = document, b = window; b = b[c] || (b[c] = {}); var d = b.maps || (b.maps = {}), r = new Set, e = new URLSearchParams, u = () => h || (h = new Promise(async (f, n) => { await (a = m.createElement("script")); e.set("libraries", [...r] + ""); for (k in g) e.set(k.replace(/[A-Z]/g, t => "_" + t[0].toLowerCase()), g[k]); e.set("callback", c + ".maps." + q); a.src = `https://maps.${c}apis.com/maps/api/js?` + e; d[q] = f; a.onerror = () => h = n(Error(p + " could not load.")); a.nonce = m.querySelector("script[nonce]")?.nonce || ""; m.head.append(a) })); d[l] ? console.warn(p + " only loads once. Ignoring:", g) : d[l] = (f, ...n) => r.add(f) && u().then(() => d[l](f, ...n)) })({
        key: "AIzaSyAOacv_xm8875Kv69dQpWanhvZfzz7dgXA",
        v: "weekly",
        // Use the 'v' parameter to indicate the version to use (weekly, beta, alpha, etc.).
    });
</script>
 */
