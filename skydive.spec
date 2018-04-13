%global import_path     github.com/skydive-project/skydive
%global gopath          %{_datadir}/gocode

%if !%{defined gobuild}
%define gobuild(o:) go build -compiler gc -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

%if !%{defined gotest}
%define gotest() go test -compiler gc -ldflags "${LDFLAGS:-}" %{?**};
%endif

# commit or tagversion need to be defined on command line
%if %{defined commit}
%define source %{commit}
%define tag 0.git%{commit}
%endif

%if %{defined tagversion}
%define source %{tagversion}
%endif

%{!?tagversion:%global tagversion 0.17.0}
%{!?source:%global source 0.17.0}
%{!?tag:%global tag 1}

Name:           skydive
Version:        %{tagversion}
Release:        %{tag}%{?dist}
Summary:        Real-time network topology and protocols analyzer.
License:        ASL 2.0
URL:            https://%{import_path}
Source0:        https://%{import_path}/releases/download/v%{source}/skydive-%{source}.tar.gz
BuildRequires:  systemd
BuildRequires:  libpcap-devel libxml2-devel
BuildRequires:  llvm clang kernel-headers

# This is used by the specfile-update-bundles script to automatically
# generate the list of the Go libraries bundled into the Skydive binaries
Provides: bundled(golang(github.com/Microsoft/go-winio)) = fff283ad5116362ca252298cfc9b95828956d85d
Provides: bundled(golang(github.com/PuerkitoBio/purell)) = fd18e053af8a4ff11039269006e8037ff374ce0e
Provides: bundled(golang(github.com/PuerkitoBio/urlesc)) = de5bf2ad457846296e2031421a34e2568e304e35
Provides: bundled(golang(github.com/Sirupsen/logrus)) = 4b6ea7319e214d98c938f12692336f7ca9348d6b
Provides: bundled(golang(github.com/StackExchange/wmi)) = 5d049714c4a64225c3c79a7cf7d02f7fb5b96338
Provides: bundled(golang(github.com/abbot/go-http-auth)) = ca62df34b58d26b6a064246c21c0a18f97813173
Provides: bundled(golang(github.com/araddon/gou)) = 0c2ab7394d785afff14c983fedce4be70ccc431f
Provides: bundled(golang(github.com/armon/consul-api)) = dcfedd50ed5334f96adee43fc88518a4f095e15c
Provides: bundled(golang(github.com/beorn7/perks/quantile)) = b965b613227fddccbfffe13eae360ed3fa822f8d
Provides: bundled(golang(github.com/bitly/go-hostpool)) = d0e59c22a56e8dadfed24f74f452cea5a52722d2
Provides: bundled(golang(github.com/cenk/hub)) = 11382a9960d39b0ecda16fd01c424c11ff765a34
Provides: bundled(golang(github.com/cenk/rpc2)) = 7ab76d2e88c77ca1a715756036d8264b2886acd2
Provides: bundled(golang(github.com/cenk/rpc2/jsonrpc)) = 7ab76d2e88c77ca1a715756036d8264b2886acd2
Provides: bundled(golang(github.com/cnf/structhash)) = 7710f1f78fb9c581deeeab57ecfb7978901b36bc
Provides: bundled(golang(github.com/cockroachdb/cmux)) = 30d10be492927e2dcae0089c374c455d42414fcb
Provides: bundled(golang(github.com/coreos/bbolt)) = 32c383e75ce054674c53b5a07e55de85332aee14
Provides: bundled(golang(github.com/coreos/etcd/alarm)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/auth)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/auth/authpb)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/client)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/clientv3)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/clientv3/concurrency)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/compactor)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/discovery)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/embed)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/error)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/etcdhttp)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/v2http)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/v2http/httptypes)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/v3client)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/v3election)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/v3election/v3electionpb)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/v3election/v3electionpb/gw)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/v3lock)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/v3lock/v3lockpb)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/v3lock/v3lockpb/gw)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/v3rpc)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/v3rpc/rpctypes)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/auth)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/etcdserverpb)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/etcdserverpb/gw)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/membership)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/stats)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/lease)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/lease/leasehttp)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/lease/leasepb)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/mvcc)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/mvcc/backend)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/mvcc/mvccpb)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/adt)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/contention)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/cors)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/cpuutil)) = 1b3ac99e8a431b381e633802cc42fe70e663baf5
Provides: bundled(golang(github.com/coreos/etcd/pkg/crc)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/debugutil)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/fileutil)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/httputil)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/idutil)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/ioutil)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/logutil)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/monotime)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/netutil)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/osutil)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/pathutil)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/pbutil)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/runtime)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/schedule)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/srv)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/tlsutil)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/transport)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/types)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/pkg/wait)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/proxy/grpcproxy/adapter)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/raft)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/raft/raftpb)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/rafthttp)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/snap)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/snap/snappb)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/store)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/version)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/wal)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/etcd/wal/walpb)) = b5abfe1858ddde05b83b96a810dc2b50cc5fcd94
Provides: bundled(golang(github.com/coreos/go-semver)) = 8ab6407b697782a06568d4b7f1db25550ec2e4c6
Provides: bundled(golang(github.com/coreos/go-semver/semver)) = 8ab6407b697782a06568d4b7f1db25550ec2e4c6
Provides: bundled(golang(github.com/coreos/go-systemd/journal)) = 7b2428fec40033549c68f54e26e89e7ca9a9ce31
Provides: bundled(golang(github.com/coreos/pkg/capnslog)) = 66fe44ad037ccb80329115cb4db0dbe8e9beb03a
Provides: bundled(golang(github.com/davecgh/go-spew/spew)) = 346938d642f2ec3594ed81d874461961cd0faa76
Provides: bundled(golang(github.com/dgrijalva/jwt-go)) = d2709f9f1f31ebcda9651b03077758c1f3a0018c
Provides: bundled(golang(github.com/docker/distribution/digest)) = 325b0804fef3a66309d962357aac3c2ce3f4d329
Provides: bundled(golang(github.com/docker/distribution/reference)) = 325b0804fef3a66309d962357aac3c2ce3f4d329
Provides: bundled(golang(github.com/docker/docker/api/types)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/api/types/blkiodev)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/api/types/container)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/api/types/events)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/api/types/filters)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/api/types/mount)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/api/types/network)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/api/types/reference)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/api/types/registry)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/api/types/strslice)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/api/types/swarm)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/api/types/time)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/api/types/versions)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/api/types/volume)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/client)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/docker/pkg/tlsconfig)) = c6d412e329c85f32a4b2269b49aaa0794affcf88
Provides: bundled(golang(github.com/docker/go-connections/nat)) = 990a1a1a70b0da4c4cb70e117971a4f0babfbf1a
Provides: bundled(golang(github.com/docker/go-connections/sockets)) = 990a1a1a70b0da4c4cb70e117971a4f0babfbf1a
Provides: bundled(golang(github.com/docker/go-connections/tlsconfig)) = 990a1a1a70b0da4c4cb70e117971a4f0babfbf1a
Provides: bundled(golang(github.com/docker/go-units)) = 5d2041e26a699eaca682e2ea41c8f891e1060444
Provides: bundled(golang(github.com/emicklei/go-restful)) = 68c9750c36bb8cb433f1b88c807b4b30df4acc40
Provides: bundled(golang(github.com/emicklei/go-restful-swagger12)) = 7524189396c68dc4b04d53852f9edc00f816b123
Provides: bundled(golang(github.com/emicklei/go-restful/log)) = 68c9750c36bb8cb433f1b88c807b4b30df4acc40
Provides: bundled(golang(github.com/fatih/structs)) = f5faa72e73092639913f5833b75e1ac1d6bc7a63
Provides: bundled(golang(github.com/fsnotify/fsnotify)) = 30411dbcefb7a1da7e84f75530ad3abe4011b4f8
Provides: bundled(golang(github.com/ghodss/yaml)) = 0ca9ea5df5451ffdf184b4428c902747c2c11cd7
Provides: bundled(golang(github.com/gima/govalid/v1)) = 7b486932bea218beb6e85f7ed28650d283dd6ce6
Provides: bundled(golang(github.com/gima/govalid/v1/internal)) = 7b486932bea218beb6e85f7ed28650d283dd6ce6
Provides: bundled(golang(github.com/go-ole/go-ole)) = a41e3c4b706f6ae8dfbff342b06e40fa4d2d0506
Provides: bundled(golang(github.com/go-ole/go-ole/oleutil)) = a41e3c4b706f6ae8dfbff342b06e40fa4d2d0506
Provides: bundled(golang(github.com/go-openapi/jsonpointer)) = 779f45308c19820f1a69e9a4cd965f496e0da10f
Provides: bundled(golang(github.com/go-openapi/jsonreference)) = 36d33bfe519efae5632669801b180bf1a245da3b
Provides: bundled(golang(github.com/go-openapi/spec)) = 7abd5745472fff5eb3685386d5fb8bf38683154d
Provides: bundled(golang(github.com/go-openapi/swag)) = f3f9494671f93fcff853e3c6e9e948b3eb71e590
Provides: bundled(golang(github.com/gobwas/httphead)) = 01c9b01b368a438f615030bbbd5e4f9e0023e15c
Provides: bundled(golang(github.com/gobwas/pool)) = 32dbaa12caca20fad12253c30591227e04f62cdd
Provides: bundled(golang(github.com/gobwas/pool/pbufio)) = 32dbaa12caca20fad12253c30591227e04f62cdd
Provides: bundled(golang(github.com/gobwas/pool/pbytes)) = 32dbaa12caca20fad12253c30591227e04f62cdd
Provides: bundled(golang(github.com/gobwas/ws)) = 915eed3240022c5265584c55032ef1b8c8f84168
Provides: bundled(golang(github.com/gobwas/ws/wsutil)) = 915eed3240022c5265584c55032ef1b8c8f84168
Provides: bundled(golang(github.com/gogo/protobuf/proto)) = 2adc21fd136931e0388e278825291678e1d98309
Provides: bundled(golang(github.com/gogo/protobuf/sortkeys)) = 2adc21fd136931e0388e278825291678e1d98309
Provides: bundled(golang(github.com/golang/glog)) = 23def4e6c14b4da8ac2ed8007337bc5eb5007998
Provides: bundled(golang(github.com/golang/protobuf/jsonpb)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/proto)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/protoc-gen-go/descriptor)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/ptypes)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/ptypes/any)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/ptypes/duration)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/ptypes/struct)) = bbd03ef6da3a115852eaf24c8a1c46aeb39aa175
Provides: bundled(golang(github.com/golang/protobuf/ptypes/timestamp)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/google/btree)) = cc6329d4279e3f025a53a83c397d2339b5705c45
Provides: bundled(golang(github.com/google/gofuzz)) = 24818f796faf91cd76ec7bddd72458fbced7a6c1
Provides: bundled(golang(github.com/google/gopacket)) = 67a21c4470a0598531a769727aef40b870ffa128
Provides: bundled(golang(github.com/google/gopacket/layers)) = 67a21c4470a0598531a769727aef40b870ffa128
Provides: bundled(golang(github.com/google/gopacket/pcap)) = 67a21c4470a0598531a769727aef40b870ffa128
Provides: bundled(golang(github.com/google/gopacket/pcapgo)) = 67a21c4470a0598531a769727aef40b870ffa128
Provides: bundled(golang(github.com/googleapis/gnostic/OpenAPIv2)) = 41d03372f44f2bc18a72c97615a669fb60e7452a
Provides: bundled(golang(github.com/googleapis/gnostic/compiler)) = 41d03372f44f2bc18a72c97615a669fb60e7452a
Provides: bundled(golang(github.com/googleapis/gnostic/extensions)) = 41d03372f44f2bc18a72c97615a669fb60e7452a
Provides: bundled(golang(github.com/gophercloud/gophercloud)) = 849a2e71dd64dbfa2bd4be110ace68881802414b
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack)) = 849a2e71dd64dbfa2bd4be110ace68881802414b
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/identity/v2/tenants)) = 849a2e71dd64dbfa2bd4be110ace68881802414b
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/identity/v2/tokens)) = 849a2e71dd64dbfa2bd4be110ace68881802414b
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/identity/v3/tokens)) = 849a2e71dd64dbfa2bd4be110ace68881802414b
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/networking/v2/extensions/provider)) = 849a2e71dd64dbfa2bd4be110ace68881802414b
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/networking/v2/networks)) = 849a2e71dd64dbfa2bd4be110ace68881802414b
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/networking/v2/ports)) = 849a2e71dd64dbfa2bd4be110ace68881802414b
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/networking/v2/subnets)) = 849a2e71dd64dbfa2bd4be110ace68881802414b
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/utils)) = 849a2e71dd64dbfa2bd4be110ace68881802414b
Provides: bundled(golang(github.com/gophercloud/gophercloud/pagination)) = 849a2e71dd64dbfa2bd4be110ace68881802414b
Provides: bundled(golang(github.com/gorilla/context)) = 08b5f424b9271eedf6f9f0ce86cb9396ed337a42
Provides: bundled(golang(github.com/gorilla/handlers)) = 90663712d74cb411cbef281bc1e08c19d1a76145
Provides: bundled(golang(github.com/gorilla/mux)) = 5ab525f4fb1678e197ae59401e9050fa0b6cb5fd
Provides: bundled(golang(github.com/gorilla/websocket)) = cdedf21e585dae942951e34d6defc3215b4280fa
Provides: bundled(golang(github.com/gosuri/uitable)) = 36ee7e946282a3fb1cfecd476ddc9b35d8847e42
Provides: bundled(golang(github.com/gosuri/uitable/util/strutil)) = 36ee7e946282a3fb1cfecd476ddc9b35d8847e42
Provides: bundled(golang(github.com/gosuri/uitable/util/wordwrap)) = 36ee7e946282a3fb1cfecd476ddc9b35d8847e42
Provides: bundled(golang(github.com/gregjones/httpcache)) = 2bcd89a1743fd4b373f7370ce8ddc14dfbd18229
Provides: bundled(golang(github.com/gregjones/httpcache/diskcache)) = 2bcd89a1743fd4b373f7370ce8ddc14dfbd18229
Provides: bundled(golang(github.com/grpc-ecosystem/go-grpc-prometheus)) = 6b7015e65d366bf3f19b2b2a000a831940f0f7e0
Provides: bundled(golang(github.com/grpc-ecosystem/grpc-gateway/runtime)) = 8cc3a55af3bcf171a1c23a90c4df9cf591706104
Provides: bundled(golang(github.com/grpc-ecosystem/grpc-gateway/runtime/internal)) = 8cc3a55af3bcf171a1c23a90c4df9cf591706104
Provides: bundled(golang(github.com/grpc-ecosystem/grpc-gateway/utilities)) = 8cc3a55af3bcf171a1c23a90c4df9cf591706104
Provides: bundled(golang(github.com/hashicorp/golang-lru)) = 0a025b7e63adc15a622f29b0b2c4c3848243bbf6
Provides: bundled(golang(github.com/hashicorp/golang-lru/simplelru)) = 0a025b7e63adc15a622f29b0b2c4c3848243bbf6
Provides: bundled(golang(github.com/hashicorp/hcl)) = 23c074d0eceb2b8a5bfdbb271ab780cde70f05a8
Provides: bundled(golang(github.com/hashicorp/hcl/hcl/ast)) = 23c074d0eceb2b8a5bfdbb271ab780cde70f05a8
Provides: bundled(golang(github.com/hashicorp/hcl/hcl/parser)) = 23c074d0eceb2b8a5bfdbb271ab780cde70f05a8
Provides: bundled(golang(github.com/hashicorp/hcl/hcl/printer)) = 23c074d0eceb2b8a5bfdbb271ab780cde70f05a8
Provides: bundled(golang(github.com/hashicorp/hcl/hcl/scanner)) = 23c074d0eceb2b8a5bfdbb271ab780cde70f05a8
Provides: bundled(golang(github.com/hashicorp/hcl/hcl/strconv)) = 23c074d0eceb2b8a5bfdbb271ab780cde70f05a8
Provides: bundled(golang(github.com/hashicorp/hcl/hcl/token)) = 23c074d0eceb2b8a5bfdbb271ab780cde70f05a8
Provides: bundled(golang(github.com/hashicorp/hcl/json/parser)) = 23c074d0eceb2b8a5bfdbb271ab780cde70f05a8
Provides: bundled(golang(github.com/hashicorp/hcl/json/scanner)) = 23c074d0eceb2b8a5bfdbb271ab780cde70f05a8
Provides: bundled(golang(github.com/hashicorp/hcl/json/token)) = 23c074d0eceb2b8a5bfdbb271ab780cde70f05a8
Provides: bundled(golang(github.com/howeyc/gopass)) = bf9dde6d0d2c004a008c27aaee91170c786f6db8
Provides: bundled(golang(github.com/hydrogen18/stoppableListener)) = dadc9ccc400c712e5a316107a5c462863919e579
Provides: bundled(golang(github.com/imdario/mergo)) = e3000cb3d28c72b837601cac94debd91032d19fe
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = 76626ae9c91c4f2a10f34cad8ce83ea42c93bb75
Provides: bundled(golang(github.com/intel-go/yanff/asm)) = 35804adce65005f76409327527e4e256569cacc6
Provides: bundled(golang(github.com/intel-go/yanff/common)) = 35804adce65005f76409327527e4e256569cacc6
Provides: bundled(golang(github.com/intel-go/yanff/flow)) = 35804adce65005f76409327527e4e256569cacc6
Provides: bundled(golang(github.com/intel-go/yanff/low)) = 35804adce65005f76409327527e4e256569cacc6
Provides: bundled(golang(github.com/intel-go/yanff/packet)) = 35804adce65005f76409327527e4e256569cacc6
Provides: bundled(golang(github.com/intel-go/yanff/scheduler)) = 35804adce65005f76409327527e4e256569cacc6
Provides: bundled(golang(github.com/iovisor/gobpf/elf)) = dd767a9fd5f868874ed117811461410100cea403
Provides: bundled(golang(github.com/iovisor/gobpf/elf/include)) = 78e59123840b27e16b7b4e7ca54f2ce9493b7271
Provides: bundled(golang(github.com/iovisor/gobpf/pkg)) = 78e59123840b27e16b7b4e7ca54f2ce9493b7271
Provides: bundled(golang(github.com/iovisor/gobpf/pkg/bpffs)) = dd767a9fd5f868874ed117811461410100cea403
Provides: bundled(golang(github.com/iovisor/gobpf/pkg/cpuonline)) = dd767a9fd5f868874ed117811461410100cea403
Provides: bundled(golang(github.com/jbowtie/gokogiri)) = e2644e49d5b4a4d2382d1a4b28dfbb313a4ffb0c
Provides: bundled(golang(github.com/jbowtie/gokogiri/help)) = e2644e49d5b4a4d2382d1a4b28dfbb313a4ffb0c
Provides: bundled(golang(github.com/jbowtie/gokogiri/html)) = e2644e49d5b4a4d2382d1a4b28dfbb313a4ffb0c
Provides: bundled(golang(github.com/jbowtie/gokogiri/util)) = e2644e49d5b4a4d2382d1a4b28dfbb313a4ffb0c
Provides: bundled(golang(github.com/jbowtie/gokogiri/xml)) = e2644e49d5b4a4d2382d1a4b28dfbb313a4ffb0c
Provides: bundled(golang(github.com/jbowtie/gokogiri/xpath)) = e2644e49d5b4a4d2382d1a4b28dfbb313a4ffb0c
Provides: bundled(golang(github.com/jonboulle/clockwork)) = ed104f61ea4877bea08af6f759805674861e968d
Provides: bundled(golang(github.com/json-iterator/go)) = ff2b70c1dbffdd98567bd8c2f9449d97c0d04c88
Provides: bundled(golang(github.com/juju/loggo)) = 8232ab8918d91c72af1a9fb94d3edbe31d88b790
Provides: bundled(golang(github.com/juju/ratelimit)) = 5b9ff866471762aa2ab2dced63c9fb6f53921342
Provides: bundled(golang(github.com/juju/webbrowser)) = 54b8c57083b4afb7dc75da7f13e2967b2606a507
Provides: bundled(golang(github.com/julienschmidt/httprouter)) = d1898390779332322e6b5ca5011da4bf249bb056
Provides: bundled(golang(github.com/kardianos/osext)) = c2c54e542fb797ad986b31721e1baedf214ca413
Provides: bundled(golang(github.com/kr/fs)) = 2788f0dbd16903de03cb8186e5c7d97b69ad387b
Provides: bundled(golang(github.com/kr/pty)) = 95d05c1eef33a45bd58676b6ce28d105839b8d0b
Provides: bundled(golang(github.com/lxc/lxd/client)) = 9907f3a64b6b8ec9144e8be02d633b951439c0f6
Provides: bundled(golang(github.com/lxc/lxd/shared)) = 9907f3a64b6b8ec9144e8be02d633b951439c0f6
Provides: bundled(golang(github.com/lxc/lxd/shared/api)) = 9907f3a64b6b8ec9144e8be02d633b951439c0f6
Provides: bundled(golang(github.com/lxc/lxd/shared/cancel)) = 9907f3a64b6b8ec9144e8be02d633b951439c0f6
Provides: bundled(golang(github.com/lxc/lxd/shared/ioprogress)) = 9907f3a64b6b8ec9144e8be02d633b951439c0f6
Provides: bundled(golang(github.com/lxc/lxd/shared/logger)) = 9907f3a64b6b8ec9144e8be02d633b951439c0f6
Provides: bundled(golang(github.com/lxc/lxd/shared/osarch)) = 9907f3a64b6b8ec9144e8be02d633b951439c0f6
Provides: bundled(golang(github.com/lxc/lxd/shared/simplestreams)) = 9907f3a64b6b8ec9144e8be02d633b951439c0f6
Provides: bundled(golang(github.com/magiconair/properties)) = c81f9d71af8f8cba1466501d30326b99a4e56c19
Provides: bundled(golang(github.com/mailru/easyjson/buffer)) = 2a92e673c9a6302dd05c3a691ae1f24aef46457d
Provides: bundled(golang(github.com/mailru/easyjson/jlexer)) = 2a92e673c9a6302dd05c3a691ae1f24aef46457d
Provides: bundled(golang(github.com/mailru/easyjson/jwriter)) = 2a92e673c9a6302dd05c3a691ae1f24aef46457d
Provides: bundled(golang(github.com/mattbaird/elastigo)) = 441c1531dca50a19990385930149f6785f78fe59
Provides: bundled(golang(github.com/mattbaird/elastigo/lib)) = 441c1531dca50a19990385930149f6785f78fe59
Provides: bundled(golang(github.com/mattn/go-runewidth)) = d6bea18f789704b5f83375793155289da36a3c7f
Provides: bundled(golang(github.com/matttproud/golang_protobuf_extensions/pbutil)) = d0c3fe89de86839aecf2e0579c40ba3bb336a453
Provides: bundled(golang(github.com/mitchellh/go-homedir)) = 756f7b183b7ab78acdbbee5c7f392838ed459dda
Provides: bundled(golang(github.com/mitchellh/hashstructure)) = ab25296c0f51f1022f01cd99dfb45f1775de8799
Provides: bundled(golang(github.com/mitchellh/mapstructure)) = 281073eb9eb092240d33ef253c404f1cca550309
Provides: bundled(golang(github.com/nlewo/contrail-introspect-cli/collection)) = e4df28ccf9801abbe32edd5ddaba31a7a62b61b6
Provides: bundled(golang(github.com/nlewo/contrail-introspect-cli/descriptions)) = e4df28ccf9801abbe32edd5ddaba31a7a62b61b6
Provides: bundled(golang(github.com/nlewo/contrail-introspect-cli/utils)) = e4df28ccf9801abbe32edd5ddaba31a7a62b61b6
Provides: bundled(golang(github.com/nu7hatch/gouuid)) = 179d4d0c4d8d407a32af483c2354df1d2c91e6c3
Provides: bundled(golang(github.com/op/go-logging)) = 970db520ece77730c7e4724c61121037378659d9
Provides: bundled(golang(github.com/opencontainers/runc/libcontainer/user)) = 8fa5343b0058459296399a89bc532aa5508de28d
Provides: bundled(golang(github.com/pelletier/go-toml)) = 05bcc0fb0d3e60da4b8dd5bd7e0ea563eb4ca943
Provides: bundled(golang(github.com/peterbourgon/diskv)) = 2973218375c3d13162e1d3afe1708aaee318ef3f
Provides: bundled(golang(github.com/peterh/liner)) = 8975875355a81d612fafb9f5a6037bdcc2d9b073
Provides: bundled(golang(github.com/pkg/errors)) = ff09b135c25aae272398c51a07235b90a75aa4f0
Provides: bundled(golang(github.com/pkg/sftp)) = e84cc8c755ca39b7b64f510fe1fffc1b51f210a5
Provides: bundled(golang(github.com/pmylund/go-cache)) = a3647f8e31d79543b2d0f0ae2fe5c379d72cedc0
Provides: bundled(golang(github.com/prometheus/client_golang/prometheus)) = 5cec1d0429b02e4323e042eb04dafdb079ddf568
Provides: bundled(golang(github.com/prometheus/client_model/go)) = fa8ad6fec33561be4280a8f0514318c79d7f6cb6
Provides: bundled(golang(github.com/prometheus/common/expfmt)) = 23070236b1ebff452f494ae831569545c2b61d26
Provides: bundled(golang(github.com/prometheus/common/internal/bitbucket.org/ww/goautoneg)) = 23070236b1ebff452f494ae831569545c2b61d26
Provides: bundled(golang(github.com/prometheus/common/model)) = 23070236b1ebff452f494ae831569545c2b61d26
Provides: bundled(golang(github.com/prometheus/procfs)) = 406e5b7bfd8201a36e2bb5f7bdae0b03380c2ce8
Provides: bundled(golang(github.com/robertkrimen/otto)) = bf1c3795ba078da6905fe80bfbc3ed3d8c36e9aa
Provides: bundled(golang(github.com/robertkrimen/otto/ast)) = bf1c3795ba078da6905fe80bfbc3ed3d8c36e9aa
Provides: bundled(golang(github.com/robertkrimen/otto/dbg)) = bf1c3795ba078da6905fe80bfbc3ed3d8c36e9aa
Provides: bundled(golang(github.com/robertkrimen/otto/file)) = bf1c3795ba078da6905fe80bfbc3ed3d8c36e9aa
Provides: bundled(golang(github.com/robertkrimen/otto/parser)) = bf1c3795ba078da6905fe80bfbc3ed3d8c36e9aa
Provides: bundled(golang(github.com/robertkrimen/otto/registry)) = bf1c3795ba078da6905fe80bfbc3ed3d8c36e9aa
Provides: bundled(golang(github.com/robertkrimen/otto/token)) = bf1c3795ba078da6905fe80bfbc3ed3d8c36e9aa
Provides: bundled(golang(github.com/rogpeppe/fastuuid)) = 6724a57986aff9bff1a1770e9347036def7c89f6
Provides: bundled(golang(github.com/safchain/ethtool)) = e01512671ed4c2248daf0c5e974ecf88a4947335
Provides: bundled(golang(github.com/shirou/gopsutil/cpu)) = 6a368fb7cd1221fa6ea90facc9447c9a2234c255
Provides: bundled(golang(github.com/shirou/gopsutil/host)) = 6a368fb7cd1221fa6ea90facc9447c9a2234c255
Provides: bundled(golang(github.com/shirou/gopsutil/internal/common)) = 6a368fb7cd1221fa6ea90facc9447c9a2234c255
Provides: bundled(golang(github.com/shirou/gopsutil/mem)) = 6a368fb7cd1221fa6ea90facc9447c9a2234c255
Provides: bundled(golang(github.com/shirou/gopsutil/net)) = 6a368fb7cd1221fa6ea90facc9447c9a2234c255
Provides: bundled(golang(github.com/shirou/gopsutil/process)) = 6a368fb7cd1221fa6ea90facc9447c9a2234c255
Provides: bundled(golang(github.com/shirou/w32)) = bb4de0191aa41b5507caa14b0650cdbddcd9280b
Provides: bundled(golang(github.com/skydive-project/dede/dede)) = d95b69cd1f75137aab3bcc01d6facf2aa7a43b80
Provides: bundled(golang(github.com/skydive-project/dede/statics)) = d95b69cd1f75137aab3bcc01d6facf2aa7a43b80
Provides: bundled(golang(github.com/socketplane/libovsdb)) = 5113f8fb4d9d374417ab4ce35424fbea1aad7272
Provides: bundled(golang(github.com/spf13/afero)) = a80ea588265c05730645be8342eeafeaa72b2923
Provides: bundled(golang(github.com/spf13/afero/mem)) = a80ea588265c05730645be8342eeafeaa72b2923
Provides: bundled(golang(github.com/spf13/afero/sftp)) = a80ea588265c05730645be8342eeafeaa72b2923
Provides: bundled(golang(github.com/spf13/cast)) = 8965335b8c7107321228e3e3702cab9832751bac
Provides: bundled(golang(github.com/spf13/cobra)) = 9c28e4bbd74e5c3ed7aacbc552b2cab7cfdfe744
Provides: bundled(golang(github.com/spf13/jwalterweatherman)) = d00654080cddbd2b082acaa74007cb94a2b40866
Provides: bundled(golang(github.com/spf13/pflag)) = c7e63cf4530bcd3ba943729cee0efeff2ebea63f
Provides: bundled(golang(github.com/spf13/viper)) = 54676d0dbb12f9b6febb2f8210e9590d81d4b5e3
Provides: bundled(golang(github.com/spf13/viper/remote)) = 54676d0dbb12f9b6febb2f8210e9590d81d4b5e3
Provides: bundled(golang(github.com/tchap/zapext/zapsyslog)) = e61c0c8823393722ae09ce0faee42fa177088a4b
Provides: bundled(golang(github.com/tebeka/selenium)) = 657e45ec600f26e76da253936c1f2adb6978ff72
Provides: bundled(golang(github.com/tebeka/selenium/chrome)) = 657e45ec600f26e76da253936c1f2adb6978ff72
Provides: bundled(golang(github.com/tebeka/selenium/firefox)) = 657e45ec600f26e76da253936c1f2adb6978ff72
Provides: bundled(golang(github.com/tebeka/selenium/internal/zip)) = 657e45ec600f26e76da253936c1f2adb6978ff72
Provides: bundled(golang(github.com/ugorji/go/codec)) = ded73eae5db7e7a0ef6f55aace87a2873c5d2b74
Provides: bundled(golang(github.com/vishvananda/netlink)) = 016ba6f67a12c03708643150afcfb1509be7747a
Provides: bundled(golang(github.com/vishvananda/netlink/nl)) = 016ba6f67a12c03708643150afcfb1509be7747a
Provides: bundled(golang(github.com/vishvananda/netns)) = 604eaf189ee867d8c147fafc28def2394e878d25
Provides: bundled(golang(github.com/weaveworks/tcptracer-bpf)) = e080bd747dc6b62d4ed3ed2b7f0be4801bef8faf
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = 6fe8760cad3569743d51ddbb243b26f8456742dc
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = e02fc20de94c78484cd5ffb007f8af96be030a45
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = 702b404897d4364af44dc8dcabc9815947942325
Provides: bundled(golang(github.com/xiang90/probing)) = 07dd2e8dfe18522e9c447ba95f2fe95262f63bb2
Provides: bundled(golang(github.com/xordataexchange/crypt/backend)) = b2862e3d0a775f18c7cfe02273500ae307b61218
Provides: bundled(golang(github.com/xordataexchange/crypt/backend/consul)) = b2862e3d0a775f18c7cfe02273500ae307b61218
Provides: bundled(golang(github.com/xordataexchange/crypt/backend/etcd)) = b2862e3d0a775f18c7cfe02273500ae307b61218
Provides: bundled(golang(github.com/xordataexchange/crypt/config)) = b2862e3d0a775f18c7cfe02273500ae307b61218
Provides: bundled(golang(github.com/xordataexchange/crypt/encoding/secconf)) = b2862e3d0a775f18c7cfe02273500ae307b61218
Provides: bundled(golang(go.uber.org/atomic)) = 0506d69f5564c56e25797bf7183c28921d4c6360
Provides: bundled(golang(go.uber.org/multierr)) = 3c4937480c32f4c13a875a1829af76c98ca3d40a
Provides: bundled(golang(go.uber.org/zap)) = 35aad584952c3e7020db7b839f6b102de6271f89
Provides: bundled(golang(go.uber.org/zap/buffer)) = 35aad584952c3e7020db7b839f6b102de6271f89
Provides: bundled(golang(go.uber.org/zap/internal/bufferpool)) = 35aad584952c3e7020db7b839f6b102de6271f89
Provides: bundled(golang(go.uber.org/zap/internal/color)) = 35aad584952c3e7020db7b839f6b102de6271f89
Provides: bundled(golang(go.uber.org/zap/internal/exit)) = 35aad584952c3e7020db7b839f6b102de6271f89
Provides: bundled(golang(go.uber.org/zap/zapcore)) = 35aad584952c3e7020db7b839f6b102de6271f89
Provides: bundled(golang(golang.org/x/crypto/bcrypt)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/blowfish)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/cast5)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/curve25519)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/nacl/box)) = 432090b8f568c018896cd8a0fb0345872bbac6ce
Provides: bundled(golang(golang.org/x/crypto/nacl/secretbox)) = 432090b8f568c018896cd8a0fb0345872bbac6ce
Provides: bundled(golang(golang.org/x/crypto/openpgp)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/openpgp/armor)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/openpgp/elgamal)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/openpgp/errors)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/openpgp/packet)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/openpgp/s2k)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/poly1305)) = 432090b8f568c018896cd8a0fb0345872bbac6ce
Provides: bundled(golang(golang.org/x/crypto/salsa20/salsa)) = 432090b8f568c018896cd8a0fb0345872bbac6ce
Provides: bundled(golang(golang.org/x/crypto/ssh)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/ssh/terminal)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/net/bpf)) = a6577fac2d73be281a500b310739095313165611
Provides: bundled(golang(golang.org/x/net/context)) = 66aacef3dd8a676686c7ae3716979581e8b03c47
Provides: bundled(golang(golang.org/x/net/context/ctxhttp)) = 66aacef3dd8a676686c7ae3716979581e8b03c47
Provides: bundled(golang(golang.org/x/net/html)) = cbe0f9307d0156177f9dd5dc85da1a31abc5f2fb
Provides: bundled(golang(golang.org/x/net/html/atom)) = cbe0f9307d0156177f9dd5dc85da1a31abc5f2fb
Provides: bundled(golang(golang.org/x/net/http2)) = 66aacef3dd8a676686c7ae3716979581e8b03c47
Provides: bundled(golang(golang.org/x/net/http2/hpack)) = 66aacef3dd8a676686c7ae3716979581e8b03c47
Provides: bundled(golang(golang.org/x/net/idna)) = 0744d001aa8470aaa53df28d32e5ceeb8af9bd70
Provides: bundled(golang(golang.org/x/net/internal/timeseries)) = 66aacef3dd8a676686c7ae3716979581e8b03c47
Provides: bundled(golang(golang.org/x/net/lex/httplex)) = f5dfe339be1d06f81b22525fe34671ee7d2c8904
Provides: bundled(golang(golang.org/x/net/proxy)) = 6acef71eb69611914f7a30939ea9f6e194c78172
Provides: bundled(golang(golang.org/x/net/publicsuffix)) = cbe0f9307d0156177f9dd5dc85da1a31abc5f2fb
Provides: bundled(golang(golang.org/x/net/trace)) = 66aacef3dd8a676686c7ae3716979581e8b03c47
Provides: bundled(golang(golang.org/x/sys/unix)) = 810d7000345868fc619eb81f46307107118f4ae1
Provides: bundled(golang(golang.org/x/sys/windows)) = 810d7000345868fc619eb81f46307107118f4ae1
Provides: bundled(golang(golang.org/x/text/secure/bidirule)) = 1cbadb444a806fd9430d14ad08967ed91da4fa0a
Provides: bundled(golang(golang.org/x/text/transform)) = ab5ac5f9a8deb4855a60fab02bc61a4ec770bd49
Provides: bundled(golang(golang.org/x/text/unicode/bidi)) = 1cbadb444a806fd9430d14ad08967ed91da4fa0a
Provides: bundled(golang(golang.org/x/text/unicode/norm)) = 02704b6b714738b763ba478766eb55a4b4851cd4
Provides: bundled(golang(golang.org/x/text/width)) = ab5ac5f9a8deb4855a60fab02bc61a4ec770bd49
Provides: bundled(golang(google.golang.org/genproto/googleapis/api/annotations)) = 2b5a72b8730b0b16380010cfe5286c42108d88e7
Provides: bundled(golang(google.golang.org/genproto/googleapis/rpc/status)) = 2b5a72b8730b0b16380010cfe5286c42108d88e7
Provides: bundled(golang(google.golang.org/grpc)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/balancer)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/codes)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/connectivity)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/credentials)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/grpclb/grpc_lb_v1/messages)) = d50734d1d6ca477a72646f3022216ec39639f4cd
Provides: bundled(golang(google.golang.org/grpc/grpclog)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/health/grpc_health_v1)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/internal)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/keepalive)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/metadata)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/naming)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/peer)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/resolver)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/stats)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/status)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/tap)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(google.golang.org/grpc/transport)) = 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
Provides: bundled(golang(gopkg.in/errgo.v1)) = 442357a80af5c6bf9b6d51ae791a39c3421004f3
Provides: bundled(golang(gopkg.in/fsnotify/fsnotify.v1)) = c2828203cd70a50dcccfb2761f8b1f8ceef9a8e9
Provides: bundled(golang(gopkg.in/httprequest.v1)) = 93f8fee4081f01ea23d258bdbbcdd319f668d718
Provides: bundled(golang(gopkg.in/inf.v0)) = 3887ee99ecf07df5b447e9b00d9c0b2adaa9f3e4
Provides: bundled(golang(gopkg.in/macaroon-bakery.v2/bakery)) = 22c04a94d902625448265ef041bb53e715452a40
Provides: bundled(golang(gopkg.in/macaroon-bakery.v2/bakery/checkers)) = 22c04a94d902625448265ef041bb53e715452a40
Provides: bundled(golang(gopkg.in/macaroon-bakery.v2/bakery/internal/macaroonpb)) = 22c04a94d902625448265ef041bb53e715452a40
Provides: bundled(golang(gopkg.in/macaroon-bakery.v2/httpbakery)) = 22c04a94d902625448265ef041bb53e715452a40
Provides: bundled(golang(gopkg.in/macaroon-bakery.v2/internal/httputil)) = 22c04a94d902625448265ef041bb53e715452a40
Provides: bundled(golang(gopkg.in/macaroon.v2)) = bed2a428da6e56d950bed5b41fcbae3141e5b0d0
Provides: bundled(golang(gopkg.in/sourcemap.v1)) = eef8f47ab679652a7d3a4ee34c34314d255d2536
Provides: bundled(golang(gopkg.in/sourcemap.v1/base64vlq)) = eef8f47ab679652a7d3a4ee34c34314d255d2536
Provides: bundled(golang(gopkg.in/urfave/cli.v2)) = b2bf3c5abeb90da407891aecd1df2c5a1f6170c1
Provides: bundled(golang(gopkg.in/validator.v2)) = 3e4f037f12a1221a0864cf0dd2e81c452ab22448
Provides: bundled(golang(gopkg.in/yaml.v2)) = bef53efd0c76e49e6de55ead051f886bea7e9420
Provides: bundled(golang(k8s.io/api/admissionregistration/v1alpha1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/apps/v1beta1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/apps/v1beta2)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/authentication/v1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/authentication/v1beta1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/authorization/v1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/authorization/v1beta1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/autoscaling/v1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/autoscaling/v2beta1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/batch/v1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/batch/v1beta1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/batch/v2alpha1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/certificates/v1beta1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/core/v1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/extensions/v1beta1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/networking/v1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/policy/v1beta1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/rbac/v1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/rbac/v1alpha1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/rbac/v1beta1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/scheduling/v1alpha1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/settings/v1alpha1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/storage/v1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/api/storage/v1beta1)) = 4df58c811fe2e65feb879227b2b245e4dc26e7ad
Provides: bundled(golang(k8s.io/apimachinery/pkg/api/equality)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/api/errors)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/api/meta)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/api/resource)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/internalversion)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/v1)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/v1alpha1)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/conversion)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/conversion/queryparams)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/conversion/unstructured)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/fields)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/labels)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/schema)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/json)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/protobuf)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/recognizer)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/streaming)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/versioning)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/selection)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/types)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/cache)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/clock)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/diff)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/errors)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/framer)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/intstr)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/json)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/net)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/runtime)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/sets)) = 18a564baac720819100827c16fdebcadb05b2d0d
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/validation)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/validation/field)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/wait)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/yaml)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/version)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/pkg/watch)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/apimachinery/third_party/forked/golang/reflect)) = 019ae5ada31de202164b118aee88ee2d14075c31
Provides: bundled(golang(k8s.io/client-go/discovery)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/scheme)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/admissionregistration/v1alpha1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/apps/v1beta1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/apps/v1beta2)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authentication/v1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authentication/v1beta1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authorization/v1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authorization/v1beta1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/autoscaling/v1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/autoscaling/v2beta1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/batch/v1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/batch/v1beta1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/batch/v2alpha1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/certificates/v1beta1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/core/v1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/extensions/v1beta1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/networking/v1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/policy/v1beta1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/rbac/v1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/rbac/v1alpha1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/rbac/v1beta1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/scheduling/v1alpha1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/settings/v1alpha1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/storage/v1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/storage/v1beta1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/pkg/version)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/rest)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/rest/watch)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/tools/auth)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/tools/cache)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/tools/clientcmd)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/tools/clientcmd/api)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/tools/clientcmd/api/latest)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/tools/clientcmd/api/v1)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/tools/metrics)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/tools/pager)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/tools/reference)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/transport)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/util/cert)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/util/flowcontrol)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/util/homedir)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/client-go/util/integer)) = 35ccd4336052e7d73018b1382413534936f34eee
Provides: bundled(golang(k8s.io/kube-openapi/pkg/common)) = 39a7bf85c140f972372c2a0d1ee40adbf0c8bfe1

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang} >= 1.8

%description
Skydive is an open source real-time network topology and protocols analyzer.
It aims to provide a comprehensive way of what is happening in the network
infrastrure.

Skydive agents collect topology informations and flows and forward them to a
central agent for further analysis. All the informations are stored in an
Elasticsearch database.

Skydive is SDN-agnostic but provides SDN drivers in order to enhance the
topology and flows informations.

%package analyzer
Summary:          Skydive analyzer
Requires:         %{name} = %{version}-%{release}
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description analyzer
Collects data captured by the Skydive agents.

%package agent
Summary:          Skydive agent
Requires:         %{name} = %{version}-%{release}
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description agent
The Skydive agent has to be started on each node where the topology and
flows informations will be captured.

%package ansible
Summary:          Skydive ansible recipes
Requires:         %{name} = %{version}-%{release}
Requires:         ansible

%description ansible
Ansible recipes to deploy Skydive

%prep
%setup -q -n skydive-%{source}/src/%{import_path}

%build
export GOPATH=%{_builddir}/skydive-%{source}
export GO15VENDOREXPERIMENT=1
%gobuild -o bin/skydive %{import_path}
bin/skydive bash-completion

%install
export GOPATH=%{_builddir}/skydive-%{source}
install -D -p -m 755 bin/skydive %{buildroot}%{_bindir}/skydive
ln -s skydive %{buildroot}%{_bindir}/skydive-cli
for bin in agent analyzer
do
  install -D -m 644 contrib/systemd/skydive-${bin}.service %{buildroot}%{_unitdir}/skydive-${bin}.service
  install -D -m 644 contrib/packaging/rpm/skydive-${bin}.sysconfig %{buildroot}/%{_sysconfdir}/sysconfig/skydive-${bin}
done
install -D -m 644 etc/skydive.yml.default %{buildroot}/%{_sysconfdir}/skydive/skydive.yml
install -D -m 644 skydive-bash-completion.sh %{buildroot}/%{_sysconfdir}/bash_completion.d/skydive-bash-completion.sh
install -d -m 755 %{buildroot}/%{_datadir}/skydive-ansible
cp -R contrib/ansible/* %{buildroot}/%{_datadir}/skydive-ansible/

%post agent
%systemd_post %{basename:%{name}-agent.service}

%preun agent
%systemd_preun %{basename:%{name}-agent.service}

%postun agent
%systemd_postun

%post analyzer
%systemd_post %{basename:%{name}-analyzer.service}

%preun analyzer
%systemd_preun %{basename:%{name}-analyzer.service}

%postun analyzer
%systemd_postun

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%gotest $(go list ./... | grep -v '/tests' | grep -v '/vendor/')
%endif

%files
%doc README.md LICENSE CHANGELOG.md
%{_bindir}/skydive
%{_bindir}/skydive-cli
%{_sysconfdir}/bash_completion.d/skydive-bash-completion.sh
%config(noreplace) %{_sysconfdir}/skydive/skydive.yml

%files agent
%config(noreplace) %{_sysconfdir}/sysconfig/skydive-agent
%{_unitdir}/skydive-agent.service

%files analyzer
%config(noreplace) %{_sysconfdir}/sysconfig/skydive-analyzer
%{_unitdir}/skydive-analyzer.service

%files ansible
%{_datadir}/skydive-ansible

%changelog
* Tue Apr 03 2018 Sylvain Afchain <safchain@redhat.com> - 0.17.0-1
- Bump to version 0.17.0

* Mon Jan 29 2018 Sylvain Baubeau <sbaubeau@redhat.com> - 0.16.0-1
- Bump to version 0.16.0

* Tue Dec 5 2017 Sylvain Baubeau <sbaubeau@redhat.com> - 0.15.0-1
- Bump to version 0.15.0

* Tue Nov 14 2017 Sylvain Baubeau <sbaubeau@redhat.com> - 0.14.0-1
- Bump to version 0.14.0

* Wed Oct 11 2017 Sylvain Baubeau <sbaubeau@redhat.com> - 0.13.0-1
- Bump to version 0.13.0
- Add skydive-ansible subpackage

* Fri Jul 28 2017 Sylvain Baubeau <sbaubeau@redhat.com> - 0.12.0-1
- Bump to version 0.12.0

* Fri May 5 2017 Sylvain Baubeau <sbaubeau@redhat.com> - 0.11.0-1
- Bump to version 0.11.0

* Thu Mar 30 2017 Sylvain Baubeau <sbaubeau@redhat.com> - 0.10.0-1
- Bump to version 0.10.0

* Fri Jan 27 2017 Sylvain Baubeau <sbaubeau@redhat.com> - 0.9.0-1
- Bump to version 0.9.0
- Use Fedora golang macros and guidelines for packaging

* Fri Dec 9 2016 Sylvain Baubeau <sbaubeau@redhat.com> - 0.8.0-1
- Bump to version 0.8.0

* Tue Nov 8 2016 Sylvain Baubeau <sbaubeau@redhat.com> - 0.7.0-1
- Bump to version 0.7.0

* Thu Oct 6 2016 Sylvain Baubeau <sbaubeau@redhat.com> - 0.6.0-1
- Bump to version 0.6.0

* Thu Sep 15 2016 Sylvain Baubeau <sbaubeau@redhat.com> - 0.5.0-1
- Bump to version 0.5.0

* Thu Aug 4 2016 Sylvain Baubeau <sbaubeau@redhat.com> - 0.4.0-1
- Bump to version 0.4.0

* Fri Jul 29 2016 Nicolas Planel <nplanel@redhat.com> - 0.3.0-2
- Update spec file to use govendor on go version >=1.5

* Wed Apr 27 2016 Sylvain Baubeau <sbaubeau@redhat.com> - 0.3.0-1
- Bump to version 0.3.0

* Fri Mar 25 2016 Sylvain Baubeau <sbaubeau@redhat.com> - 0.2.0-1
- Bump to version 0.2.0

* Mon Feb 1 2016 Sylvain Baubeau <sbaubeau@redhat.com> - 0.1.0-1
- Initial release of RPM

