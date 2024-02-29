const $ = document.querySelectorAll.bind(document)

const colors = [
    '#c8d6e5', // ballerina
    '#576574', // fuel
    '#54a0ff', // joust
    '#ff6b6b', // pastel
    '#1dd1a1', // wild
    '#5f27cd', // nasu
    '#00d2d3', // dust
    '#feca57', // casandora
    '#ff9ff3', // jigglypuff
    '#10ac84', // mountain
    '#48dbfb', // cyan
    '#2e86de', // bleu
    '#ee5253', // amour
    '#341f97', // bluebell
    '#ff9f43', // double dragon
    '#f368e0', // lian lotus
    '#0abde3', // cyanite
    '#01a3a4', // aqua velvet
    '#8395a7', // storm
    '#222f3e' // imperial
]

function range(start, end, steps = 10) {
    const step = (end - start) / (steps - 1)
    return Array.from({ length: steps }, (_, i) => +(start + step * i).toFixed(12))
}

let chart

function graphicate({ xValues, initialFunction, polys }) {
    const lineConfig = {
        fill: false,
        tension: 0.2,
        borderWidth: 2
    }

    chart?.destroy?.()

    chart = new Chart($('#chart-target'), {
        type: 'line',
        data: {
            labels: xValues,
            datasets: [
                {
                    ...lineConfig,
                    label: 'Original function',
                    data: xValues.map(initialFunction),
                    borderColor: '#badc58', // au: june
                    borderWidth: 3,
                    backgroundColor: '#badc58'
                },
                ...polys.map((f, i) => ({
                    ...lineConfig,
                    label: `Order ${i}`,
                    data: xValues.map(f),
                    borderColor: colors[i],
                    backgroundColor: colors[i]
                }))
            ]
        },
        options: {
            interaction: {
                intersect: false,
                mode: 'index'
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: ({ dataset, parsed }) => `${dataset.label}: ${+parsed.y.toFixed(8)}`
                    }
                }
            }
        }
    })
}
