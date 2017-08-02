%global import_path     github.com/skydive-project/skydive
%global gopath          %{_datadir}/gocode

%if !%{defined gobuild}
%define gobuild(o:) go build -compiler gc -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

%if !%{defined gotest}
%define gotest() go test -compiler gc -ldflags "${LDFLAGS:-}" %{?**};
%endif

%{!?tagversion:%global tagversion 0.12.0}

# commit or tagversion need to be defined on command line
%if %{defined commit}
%define source %{commit}
%define tag 0.git%{commit}
%endif

%if %{defined tagversion}
%define source %{tagversion}
%endif

%{!?source:%global source 0.12.0}
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

# This is used by the specfile-update-bundles script to automatically
# generate the list of the Go libraries bundled into the Skydive binaries
Provides: bundled(golang(github.com/Microsoft/go-winio)) = fff283ad5116362ca252298cfc9b95828956d85d
Provides: bundled(golang(github.com/Sirupsen/logrus)) = 4b6ea7319e214d98c938f12692336f7ca9348d6b
Provides: bundled(golang(github.com/abbot/go-http-auth)) = ca62df34b58d26b6a064246c21c0a18f97813173
Provides: bundled(golang(github.com/araddon/gou)) = 0c2ab7394d785afff14c983fedce4be70ccc431f
Provides: bundled(golang(github.com/armon/consul-api)) = dcfedd50ed5334f96adee43fc88518a4f095e15c
Provides: bundled(golang(github.com/beorn7/perks/quantile)) = b965b613227fddccbfffe13eae360ed3fa822f8d
Provides: bundled(golang(github.com/bitly/go-hostpool)) = d0e59c22a56e8dadfed24f74f452cea5a52722d2
Provides: bundled(golang(github.com/boltdb/bolt)) = 6fa1249006bd0fb3836b664614fc4bb7c6f74167
Provides: bundled(golang(github.com/cenk/hub)) = 11382a9960d39b0ecda16fd01c424c11ff765a34
Provides: bundled(golang(github.com/cenk/rpc2)) = 7ab76d2e88c77ca1a715756036d8264b2886acd2
Provides: bundled(golang(github.com/cenk/rpc2/jsonrpc)) = 7ab76d2e88c77ca1a715756036d8264b2886acd2
Provides: bundled(golang(github.com/codegangsta/cli)) = d53eb991652b1d438abdd34ce4bfa3ef1539108e
Provides: bundled(golang(github.com/coreos/etcd/alarm)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/auth)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/auth/authpb)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/client)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/compactor)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/discovery)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/error)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/etcdserver)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/v2http)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/api/v2http/httptypes)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/auth)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/etcdserverpb)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/membership)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/etcdserver/stats)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/lease)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/lease/leasehttp)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/lease/leasepb)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/mvcc)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/mvcc/backend)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/mvcc/mvccpb)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/adt)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/contention)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/crc)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/fileutil)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/httputil)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/idutil)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/ioutil)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/logutil)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/netutil)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/osutil)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/pathutil)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/pbutil)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/runtime)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/schedule)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/tlsutil)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/transport)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/types)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/pkg/wait)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/raft)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/raft/raftpb)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/rafthttp)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/snap)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/snap/snappb)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/store)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/version)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/wal)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/etcd/wal/walpb)) = 494c0126596c0e7cd59686a2e7afc90fe3296079
Provides: bundled(golang(github.com/coreos/go-etcd/etcd)) = 003851be7bb0694fe3cc457a49529a19388ee7cf
Provides: bundled(golang(github.com/coreos/go-semver)) = 8ab6407b697782a06568d4b7f1db25550ec2e4c6
Provides: bundled(golang(github.com/coreos/go-semver/semver)) = 8ab6407b697782a06568d4b7f1db25550ec2e4c6
Provides: bundled(golang(github.com/coreos/go-systemd/journal)) = 7b2428fec40033549c68f54e26e89e7ca9a9ce31
Provides: bundled(golang(github.com/coreos/pkg/capnslog)) = 66fe44ad037ccb80329115cb4db0dbe8e9beb03a
Provides: bundled(golang(github.com/davecgh/go-spew/spew)) = 346938d642f2ec3594ed81d874461961cd0faa76
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
Provides: bundled(golang(github.com/fsnotify/fsnotify)) = 30411dbcefb7a1da7e84f75530ad3abe4011b4f8
Provides: bundled(golang(github.com/gima/govalid/v1)) = 7b486932bea218beb6e85f7ed28650d283dd6ce6
Provides: bundled(golang(github.com/gima/govalid/v1/internal)) = 7b486932bea218beb6e85f7ed28650d283dd6ce6
Provides: bundled(golang(github.com/gogo/protobuf/proto)) = ff05bbbb0ff143cc11fc3f8b700fc3a2864b884d
Provides: bundled(golang(github.com/golang/protobuf/jsonpb)) = c3cefd437628a0b7d31b34fe44b3a7a540e98527
Provides: bundled(golang(github.com/golang/protobuf/proto)) = c3cefd437628a0b7d31b34fe44b3a7a540e98527
Provides: bundled(golang(github.com/google/btree)) = cc6329d4279e3f025a53a83c397d2339b5705c45
Provides: bundled(golang(github.com/google/gopacket)) = f10e8ef82a38b32acce3de1d6cec5453a2a28c74
Provides: bundled(golang(github.com/google/gopacket/layers)) = f10e8ef82a38b32acce3de1d6cec5453a2a28c74
Provides: bundled(golang(github.com/google/gopacket/pcap)) = f10e8ef82a38b32acce3de1d6cec5453a2a28c74
Provides: bundled(golang(github.com/google/gopacket/pcapgo)) = f10e8ef82a38b32acce3de1d6cec5453a2a28c74
Provides: bundled(golang(github.com/gophercloud/gophercloud)) = 19e713b71ea0ba4c56057127841ad792fe249782
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack)) = 19e713b71ea0ba4c56057127841ad792fe249782
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/identity/v2/tenants)) = 19e713b71ea0ba4c56057127841ad792fe249782
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/identity/v2/tokens)) = 19e713b71ea0ba4c56057127841ad792fe249782
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/identity/v3/tokens)) = 19e713b71ea0ba4c56057127841ad792fe249782
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/networking/v2/extensions/provider)) = 19e713b71ea0ba4c56057127841ad792fe249782
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/networking/v2/networks)) = 19e713b71ea0ba4c56057127841ad792fe249782
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/networking/v2/ports)) = 19e713b71ea0ba4c56057127841ad792fe249782
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/networking/v2/subnets)) = 19e713b71ea0ba4c56057127841ad792fe249782
Provides: bundled(golang(github.com/gophercloud/gophercloud/openstack/utils)) = 19e713b71ea0ba4c56057127841ad792fe249782
Provides: bundled(golang(github.com/gophercloud/gophercloud/pagination)) = 19e713b71ea0ba4c56057127841ad792fe249782
Provides: bundled(golang(github.com/gorilla/context)) = 1c83b3eabd45b6d76072b66b746c20815fb2872d
Provides: bundled(golang(github.com/gorilla/mux)) = 9c068cf16d982f8bd444b8c352acbeec34c4fe5b
Provides: bundled(golang(github.com/gorilla/websocket)) = 844dd6d40e1a9215ef4c8a204bfc839fcf5dd5dd
Provides: bundled(golang(github.com/gosuri/uitable)) = 36ee7e946282a3fb1cfecd476ddc9b35d8847e42
Provides: bundled(golang(github.com/gosuri/uitable/util/strutil)) = 36ee7e946282a3fb1cfecd476ddc9b35d8847e42
Provides: bundled(golang(github.com/gosuri/uitable/util/wordwrap)) = 36ee7e946282a3fb1cfecd476ddc9b35d8847e42
Provides: bundled(golang(github.com/grpc-ecosystem/grpc-gateway/runtime)) = 199c40a060d1e55508b3b85182ce6f3895ae6302
Provides: bundled(golang(github.com/grpc-ecosystem/grpc-gateway/runtime/internal)) = 199c40a060d1e55508b3b85182ce6f3895ae6302
Provides: bundled(golang(github.com/grpc-ecosystem/grpc-gateway/utilities)) = 199c40a060d1e55508b3b85182ce6f3895ae6302
Provides: bundled(golang(github.com/hashicorp/hcl)) = 1c284ec98f4b398443cbabb0d9197f7f4cc0077c
Provides: bundled(golang(github.com/hashicorp/hcl/hcl/ast)) = 1c284ec98f4b398443cbabb0d9197f7f4cc0077c
Provides: bundled(golang(github.com/hashicorp/hcl/hcl/parser)) = 1c284ec98f4b398443cbabb0d9197f7f4cc0077c
Provides: bundled(golang(github.com/hashicorp/hcl/hcl/scanner)) = 1c284ec98f4b398443cbabb0d9197f7f4cc0077c
Provides: bundled(golang(github.com/hashicorp/hcl/hcl/strconv)) = 1c284ec98f4b398443cbabb0d9197f7f4cc0077c
Provides: bundled(golang(github.com/hashicorp/hcl/hcl/token)) = 1c284ec98f4b398443cbabb0d9197f7f4cc0077c
Provides: bundled(golang(github.com/hashicorp/hcl/json/parser)) = 1c284ec98f4b398443cbabb0d9197f7f4cc0077c
Provides: bundled(golang(github.com/hashicorp/hcl/json/scanner)) = 1c284ec98f4b398443cbabb0d9197f7f4cc0077c
Provides: bundled(golang(github.com/hashicorp/hcl/json/token)) = 1c284ec98f4b398443cbabb0d9197f7f4cc0077c
Provides: bundled(golang(github.com/hydrogen18/stoppableListener)) = dadc9ccc400c712e5a316107a5c462863919e579
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = 76626ae9c91c4f2a10f34cad8ce83ea42c93bb75
Provides: bundled(golang(github.com/jbowtie/gokogiri)) = e2644e49d5b4a4d2382d1a4b28dfbb313a4ffb0c
Provides: bundled(golang(github.com/jbowtie/gokogiri/help)) = e2644e49d5b4a4d2382d1a4b28dfbb313a4ffb0c
Provides: bundled(golang(github.com/jbowtie/gokogiri/html)) = e2644e49d5b4a4d2382d1a4b28dfbb313a4ffb0c
Provides: bundled(golang(github.com/jbowtie/gokogiri/util)) = e2644e49d5b4a4d2382d1a4b28dfbb313a4ffb0c
Provides: bundled(golang(github.com/jbowtie/gokogiri/xml)) = e2644e49d5b4a4d2382d1a4b28dfbb313a4ffb0c
Provides: bundled(golang(github.com/jbowtie/gokogiri/xpath)) = e2644e49d5b4a4d2382d1a4b28dfbb313a4ffb0c
Provides: bundled(golang(github.com/jonboulle/clockwork)) = ed104f61ea4877bea08af6f759805674861e968d
Provides: bundled(golang(github.com/kardianos/osext)) = c2c54e542fb797ad986b31721e1baedf214ca413
Provides: bundled(golang(github.com/kr/fs)) = 2788f0dbd16903de03cb8186e5c7d97b69ad387b
Provides: bundled(golang(github.com/magiconair/properties)) = c81f9d71af8f8cba1466501d30326b99a4e56c19
Provides: bundled(golang(github.com/mattbaird/elastigo)) = 9dc64d2def002a03e8cbe3c4720652a5bc5ff1c0
Provides: bundled(golang(github.com/mattbaird/elastigo/lib)) = 9dc64d2def002a03e8cbe3c4720652a5bc5ff1c0
Provides: bundled(golang(github.com/mattn/go-runewidth)) = d6bea18f789704b5f83375793155289da36a3c7f
Provides: bundled(golang(github.com/matttproud/golang_protobuf_extensions/pbutil)) = d0c3fe89de86839aecf2e0579c40ba3bb336a453
Provides: bundled(golang(github.com/mitchellh/go-homedir)) = 756f7b183b7ab78acdbbee5c7f392838ed459dda
Provides: bundled(golang(github.com/mitchellh/hashstructure)) = ab25296c0f51f1022f01cd99dfb45f1775de8799
Provides: bundled(golang(github.com/mitchellh/mapstructure)) = 281073eb9eb092240d33ef253c404f1cca550309
Provides: bundled(golang(github.com/nlewo/contrail-introspect-cli/collection)) = 2196e66a7317b2f109fb5aa311a71a91231c096a
Provides: bundled(golang(github.com/nlewo/contrail-introspect-cli/descriptions)) = d18f119e1cc10d72c9bcacdc680c818dede04f69
Provides: bundled(golang(github.com/nlewo/contrail-introspect-cli/utils)) = 26910455eebfad0eccdeb8b2e0b342f1b371e82b
Provides: bundled(golang(github.com/nu7hatch/gouuid)) = 179d4d0c4d8d407a32af483c2354df1d2c91e6c3
Provides: bundled(golang(github.com/opencontainers/runc/libcontainer/user)) = 8fa5343b0058459296399a89bc532aa5508de28d
Provides: bundled(golang(github.com/pelletier/go-buffruneio)) = df1e16fde7fc330a0ca68167c23bf7ed6ac31d6d
Provides: bundled(golang(github.com/pelletier/go-toml)) = 45932ad32dfdd20826f5671da37a5f3ce9f26a8d
Provides: bundled(golang(github.com/peterh/liner)) = 8975875355a81d612fafb9f5a6037bdcc2d9b073
Provides: bundled(golang(github.com/pkg/errors)) = ff09b135c25aae272398c51a07235b90a75aa4f0
Provides: bundled(golang(github.com/pkg/sftp)) = e84cc8c755ca39b7b64f510fe1fffc1b51f210a5
Provides: bundled(golang(github.com/pmylund/go-cache)) = a122e14c4b8ee69022f62f24ba85cb36ce844366
Provides: bundled(golang(github.com/prometheus/client_golang/prometheus)) = 18acf9993a863f4c4b40612e19cdd243e7c86831
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
Provides: bundled(golang(github.com/safchain/ethtool)) = e01512671ed4c2248daf0c5e974ecf88a4947335
Provides: bundled(golang(github.com/socketplane/libovsdb)) = 5113f8fb4d9d374417ab4ce35424fbea1aad7272
Provides: bundled(golang(github.com/spf13/afero)) = a80ea588265c05730645be8342eeafeaa72b2923
Provides: bundled(golang(github.com/spf13/afero/mem)) = a80ea588265c05730645be8342eeafeaa72b2923
Provides: bundled(golang(github.com/spf13/afero/sftp)) = a80ea588265c05730645be8342eeafeaa72b2923
Provides: bundled(golang(github.com/spf13/cast)) = 2580bc98dc0e62908119e4737030cc2fdfc45e4c
Provides: bundled(golang(github.com/spf13/cobra)) = 9c28e4bbd74e5c3ed7aacbc552b2cab7cfdfe744
Provides: bundled(golang(github.com/spf13/jwalterweatherman)) = d00654080cddbd2b082acaa74007cb94a2b40866
Provides: bundled(golang(github.com/spf13/pflag)) = c7e63cf4530bcd3ba943729cee0efeff2ebea63f
Provides: bundled(golang(github.com/spf13/viper)) = 382f87b929b84ce13e9c8a375a4b217f224e6c65
Provides: bundled(golang(github.com/spf13/viper/remote)) = 382f87b929b84ce13e9c8a375a4b217f224e6c65
Provides: bundled(golang(github.com/tebeka/selenium)) = 657e45ec600f26e76da253936c1f2adb6978ff72
Provides: bundled(golang(github.com/tebeka/selenium/chrome)) = 657e45ec600f26e76da253936c1f2adb6978ff72
Provides: bundled(golang(github.com/tebeka/selenium/firefox)) = 657e45ec600f26e76da253936c1f2adb6978ff72
Provides: bundled(golang(github.com/tebeka/selenium/internal/zip)) = 657e45ec600f26e76da253936c1f2adb6978ff72
Provides: bundled(golang(github.com/ugorji/go/codec)) = b94837a2404ab90efe9289e77a70694c355739cb
Provides: bundled(golang(github.com/vishvananda/netlink)) = ebdfb7402004b397e6573c71132160d8e23cc12a
Provides: bundled(golang(github.com/vishvananda/netlink/nl)) = ebdfb7402004b397e6573c71132160d8e23cc12a
Provides: bundled(golang(github.com/vishvananda/netns)) = 604eaf189ee867d8c147fafc28def2394e878d25
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = 6fe8760cad3569743d51ddbb243b26f8456742dc
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = e02fc20de94c78484cd5ffb007f8af96be030a45
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = 702b404897d4364af44dc8dcabc9815947942325
Provides: bundled(golang(github.com/xiang90/probing)) = 6a0cc1ae81b4cc11db5e491e030e4b98fba79c19
Provides: bundled(golang(github.com/xordataexchange/crypt/backend)) = 749e360c8f236773f28fc6d3ddfce4a470795227
Provides: bundled(golang(github.com/xordataexchange/crypt/backend/consul)) = 749e360c8f236773f28fc6d3ddfce4a470795227
Provides: bundled(golang(github.com/xordataexchange/crypt/backend/etcd)) = 749e360c8f236773f28fc6d3ddfce4a470795227
Provides: bundled(golang(github.com/xordataexchange/crypt/config)) = 749e360c8f236773f28fc6d3ddfce4a470795227
Provides: bundled(golang(github.com/xordataexchange/crypt/encoding/secconf)) = 749e360c8f236773f28fc6d3ddfce4a470795227
Provides: bundled(golang(go.uber.org/atomic)) = 0506d69f5564c56e25797bf7183c28921d4c6360
Provides: bundled(golang(go.uber.org/multierr)) = 3c4937480c32f4c13a875a1829af76c98ca3d40a
Provides: bundled(golang(go.uber.org/zap)) = 4fb11c3880cea6f9634f5f22d6025e4432542fc3
Provides: bundled(golang(go.uber.org/zap/buffer)) = 4fb11c3880cea6f9634f5f22d6025e4432542fc3
Provides: bundled(golang(go.uber.org/zap/internal/bufferpool)) = 4fb11c3880cea6f9634f5f22d6025e4432542fc3
Provides: bundled(golang(go.uber.org/zap/internal/color)) = 4fb11c3880cea6f9634f5f22d6025e4432542fc3
Provides: bundled(golang(go.uber.org/zap/internal/exit)) = 4fb11c3880cea6f9634f5f22d6025e4432542fc3
Provides: bundled(golang(go.uber.org/zap/zapcore)) = 4fb11c3880cea6f9634f5f22d6025e4432542fc3
Provides: bundled(golang(golang.org/x/crypto/bcrypt)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/blowfish)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/cast5)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/curve25519)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/openpgp)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/openpgp/armor)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/openpgp/elgamal)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/openpgp/errors)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/openpgp/packet)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/openpgp/s2k)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/crypto/ssh)) = 1f22c0103821b9390939b6776727195525381532
Provides: bundled(golang(golang.org/x/net/bpf)) = a6577fac2d73be281a500b310739095313165611
Provides: bundled(golang(golang.org/x/net/context)) = 6acef71eb69611914f7a30939ea9f6e194c78172
Provides: bundled(golang(golang.org/x/net/context/ctxhttp)) = ffcf1bedda3b04ebb15a168a59800a73d6dc0f4d
Provides: bundled(golang(golang.org/x/net/http2)) = 6acef71eb69611914f7a30939ea9f6e194c78172
Provides: bundled(golang(golang.org/x/net/http2/hpack)) = 6acef71eb69611914f7a30939ea9f6e194c78172
Provides: bundled(golang(golang.org/x/net/internal/timeseries)) = 6acef71eb69611914f7a30939ea9f6e194c78172
Provides: bundled(golang(golang.org/x/net/proxy)) = 6acef71eb69611914f7a30939ea9f6e194c78172
Provides: bundled(golang(golang.org/x/net/trace)) = 6acef71eb69611914f7a30939ea9f6e194c78172
Provides: bundled(golang(golang.org/x/sys/unix)) = 99f16d856c9836c42d24e7ab64ea72916925fa97
Provides: bundled(golang(golang.org/x/sys/windows)) = 9a7256cb28ed514b4e1e5f68959914c4c28a92e0
Provides: bundled(golang(golang.org/x/text/transform)) = 02704b6b714738b763ba478766eb55a4b4851cd4
Provides: bundled(golang(golang.org/x/text/unicode/norm)) = 02704b6b714738b763ba478766eb55a4b4851cd4
Provides: bundled(golang(google.golang.org/grpc)) = b7f1379d3cbbbeb2ca3405852012e237aa05459e
Provides: bundled(golang(google.golang.org/grpc/codes)) = b7f1379d3cbbbeb2ca3405852012e237aa05459e
Provides: bundled(golang(google.golang.org/grpc/credentials)) = b7f1379d3cbbbeb2ca3405852012e237aa05459e
Provides: bundled(golang(google.golang.org/grpc/grpclog)) = b7f1379d3cbbbeb2ca3405852012e237aa05459e
Provides: bundled(golang(google.golang.org/grpc/internal)) = 13edeeffdea7a41d5aad96c28deb4c7bd01a9397
Provides: bundled(golang(google.golang.org/grpc/metadata)) = b7f1379d3cbbbeb2ca3405852012e237aa05459e
Provides: bundled(golang(google.golang.org/grpc/naming)) = 13edeeffdea7a41d5aad96c28deb4c7bd01a9397
Provides: bundled(golang(google.golang.org/grpc/peer)) = b7f1379d3cbbbeb2ca3405852012e237aa05459e
Provides: bundled(golang(google.golang.org/grpc/transport)) = b7f1379d3cbbbeb2ca3405852012e237aa05459e
Provides: bundled(golang(gopkg.in/fsnotify.v1)) = 8611c35ab31c1c28aa903d33cf8b6e44a399b09e
Provides: bundled(golang(gopkg.in/sourcemap.v1)) = eef8f47ab679652a7d3a4ee34c34314d255d2536
Provides: bundled(golang(gopkg.in/sourcemap.v1/base64vlq)) = eef8f47ab679652a7d3a4ee34c34314d255d2536
Provides: bundled(golang(gopkg.in/validator.v2)) = 3e4f037f12a1221a0864cf0dd2e81c452ab22448
Provides: bundled(golang(gopkg.in/yaml.v2)) = bef53efd0c76e49e6de55ead051f886bea7e9420

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang} >= 1.5

%description
Skydive is an open source real-time network topology and protocols analyzer.
It aims to provide a comprehensive way of what is happening in the network
infrastrure.

Skydive agents collect topology informations and flows and forward them to a
central agent for further analysis. All the informations are stored in an
Elasticsearch database.

Skydive is SDN-agnostic but provides SDN drivers in order to enhance the
topology and flows informations. Currently only the Neutron driver is provided
but more drivers will come soon.

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

%prep
%setup -q -n skydive-%{source}/src/%{import_path}

%build
export GOPATH=%{_builddir}/skydive-%{source}
export GO15VENDOREXPERIMENT=1
%gobuild -o bin/skydive %{import_path}
go run cmd/completion/completion.go

%install
export GOPATH=%{_builddir}/skydive-%{source}
install -D -p -m 755 bin/skydive %{buildroot}%{_bindir}/skydive
for bin in agent analyzer
do
  install -D -m 644 contrib/systemd/skydive-${bin}.service %{buildroot}%{_unitdir}/skydive-${bin}.service
  install -D -m 644 contrib/packaging/rpm/skydive-${bin}.sysconfig %{buildroot}/%{_sysconfdir}/sysconfig/skydive-${bin}
done
install -D -m 644 etc/skydive.yml.default %{buildroot}/%{_sysconfdir}/skydive/skydive.yml
install -D -m 644 skydive-bash-completion.sh %{buildroot}/%{_sysconfdir}/bash_completion.d/skydive-bash-completion.sh

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
%{_sysconfdir}/bash_completion.d/skydive-bash-completion.sh
%config(noreplace) %{_sysconfdir}/skydive/skydive.yml

%files agent
%config(noreplace) %{_sysconfdir}/sysconfig/skydive-agent
%{_unitdir}/skydive-agent.service

%files analyzer
%config(noreplace) %{_sysconfdir}/sysconfig/skydive-analyzer
%{_unitdir}/skydive-analyzer.service

%changelog
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
