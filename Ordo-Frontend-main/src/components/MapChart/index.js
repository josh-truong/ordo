import React, { useEffect, useState, memo } from "react";
import { csv } from "d3-fetch";
import { scaleLinear } from "d3-scale";
import {
    ComposableMap,
    Geographies,
    Geography,
    Graticule,
    ZoomableGroup
} from "react-simple-maps";

const geoUrl =
    "https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json";

// Remove this once you have new data
const rounded = num => {
    if (num > 1000000000) {
        return Math.round(num / 100000000) / 10 + "%";
    } else if (num > 1000000) {
        return Math.round(num / 100000) / 10 + "%";
    } else {
        return Math.round(num / 100) / 10 + "%";
    }
};

const colorScale = scaleLinear()
    .domain([0.29, 0.68])
    .range(["#ffedea", "#ff5233"]);

const MapChart = ({ setTooltipContent }) => {
    const [data, setData] = useState([]);

    useEffect(() => {
        // rm code here and replace with api calls to db
        // setCountries data from 0-1
        // Minimum requirements
            // Array Type
                // Column names ("ISO3", "Name")
        csv(`/vulnerability.csv`).then((data) => {
            setData(data);
        });
    }, []);

    return (
        <ComposableMap
            data-tip=""
            projectionConfig={{
                rotate: [-10, 0, 0],
                scale: 147
            }}
        >
            <ZoomableGroup zoom={1}>
                <Graticule stroke="#E4E5E6" strokeWidth={0.5} />
                {data.length > 0 && (
                    <Geographies geography={geoUrl}>
                        {({ geographies }) =>
                            geographies.map((geo) => {
                                const d = data.find((s) => s.ISO3 === geo.properties.ISO_A3);
                                return (
                                    <Geography
                                        key={geo.rsmKey}
                                        geography={geo}
                                        onMouseEnter={() => {
                                            const { NAME, POP_EST } = geo.properties;
                                            setTooltipContent(`${NAME} — ${rounded(POP_EST)}`);
                                        }}
                                        onMouseLeave={() => {
                                            setTooltipContent("");
                                        }}
                                        style={{
                                            default: {
                                                fill: `${d ? colorScale(d["2017"]) : "#F5F4F6"}`
                                            },
                                            hover: {
                                                fill: "#39FF14"
                                            }
                                        }}
                                    />
                                );
                            })
                        }
                    </Geographies>
                )}
            </ZoomableGroup>
        </ComposableMap >
    );
};

export default memo(MapChart);
