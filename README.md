# Payload Rewrite Proxy


### use case

given a template like
```
{
	"param1" => "::param1::"
}
```

the proxy will resolve and forward each request in the form of
`localhost:8000?param1=1` 
as:
`example.com` with POST data consisting of the said template having all `::placeholders::` replaced with their values provided in the GET (`param1=1`)


### motivation

a need of utility script helping do security researches for all kinds of injections, without rewriting any already existing tool, just using it via the proxy
