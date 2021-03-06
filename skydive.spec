%global import_path     github.com/skydive-project/skydive
%global gopath          %{_datadir}/gocode

%if 0%{?fedora} >= 27
%define with_features WITH_EBPF=true
%endif
%{!?with_features:%global with_features %{nil}}

%if !%{defined gotest}
%define gotest() go test -compiler gc -ldflags "${LDFLAGS:-}" %{?**};
%endif

%define extracttag() %(eval "echo %1 | cut -s -d '-' -f 2-")
%define extractversion() %(eval "echo %1 | cut -d '-' -f 1")
%define normalize() %(eval "echo %1 | tr '-' '.'")

%global selinuxtype targeted
%global selinux_policyver 3.13.1-192
%global moduletype contrib

%if 0%{?fedora} >= 27
%global selinux_semanage_pkg policycoreutils-python-utils
%else
%global selinux_semanage_pkg policycoreutils-python
%endif

%if %{defined fullver}
%define vertag %extracttag %{fullver}
%if "%{vertag}" != ""
%define tag %normalize 0.%{vertag}
%endif
%endif

%{!?fullver:%global fullver 0.19.0}
%define version %{extractversion %{fullver}}
%{!?tag:%global tag 1}

Name:           skydive
Version:        %{version}
Release:        %{tag}%{?dist}
Summary:        Real-time network topology and protocols analyzer.
License:        ASL 2.0
URL:            https://%{import_path}
Source0:        https://%{import_path}/releases/download/v%{version}/skydive-%{fullver}.tar.gz
BuildRequires:  systemd
BuildRequires:  libpcap-devel libxml2-devel
%if 0%{?fedora} >= 27
BuildRequires:  llvm clang kernel-headers
%endif
BuildRequires:  selinux-policy-devel, policycoreutils-devel
Requires:       %{name}-selinux = %{version}-%{release}

# This is used by the specfile-update-bundles script to automatically
# generate the list of the Go libraries bundled into the Skydive binaries
Provides: bundled(golang(github.com/GehirnInc/crypt)) = 5a3fafaa7c86150c096504f50630ca6ac8cff681
Provides: bundled(golang(github.com/GehirnInc/crypt/common)) = 5a3fafaa7c86150c096504f50630ca6ac8cff681
Provides: bundled(golang(github.com/GehirnInc/crypt/internal)) = 5a3fafaa7c86150c096504f50630ca6ac8cff681
Provides: bundled(golang(github.com/GehirnInc/crypt/md5_crypt)) = 5a3fafaa7c86150c096504f50630ca6ac8cff681
Provides: bundled(golang(github.com/Knetic/govaluate)) = 9aa49832a739dcd78a5542ff189fb82c3e423116
Provides: bundled(golang(github.com/Microsoft/go-winio)) = fff283ad5116362ca252298cfc9b95828956d85d
Provides: bundled(golang(github.com/PuerkitoBio/purell)) = fd18e053af8a4ff11039269006e8037ff374ce0e
Provides: bundled(golang(github.com/PuerkitoBio/urlesc)) = de5bf2ad457846296e2031421a34e2568e304e35
Provides: bundled(golang(github.com/Sirupsen/logrus)) = 4b6ea7319e214d98c938f12692336f7ca9348d6b
Provides: bundled(golang(github.com/StackExchange/wmi)) = 5d049714c4a64225c3c79a7cf7d02f7fb5b96338
Provides: bundled(golang(github.com/abbot/go-http-auth)) = ca62df34b58d26b6a064246c21c0a18f97813173
Provides: bundled(golang(github.com/armon/consul-api)) = dcfedd50ed5334f96adee43fc88518a4f095e15c
Provides: bundled(golang(github.com/beorn7/perks/quantile)) = b965b613227fddccbfffe13eae360ed3fa822f8d
Provides: bundled(golang(github.com/casbin/casbin)) = 3a17f2855cc12ad36fd614c590b9d18f46dfd65d
Provides: bundled(golang(github.com/casbin/casbin/config)) = 3a17f2855cc12ad36fd614c590b9d18f46dfd65d
Provides: bundled(golang(github.com/casbin/casbin/file-adapter)) = 3a17f2855cc12ad36fd614c590b9d18f46dfd65d
Provides: bundled(golang(github.com/casbin/casbin/model)) = 3a17f2855cc12ad36fd614c590b9d18f46dfd65d
Provides: bundled(golang(github.com/casbin/casbin/persist)) = 3a17f2855cc12ad36fd614c590b9d18f46dfd65d
Provides: bundled(golang(github.com/casbin/casbin/rbac)) = 3a17f2855cc12ad36fd614c590b9d18f46dfd65d
Provides: bundled(golang(github.com/casbin/casbin/rbac/default-role-manager)) = 3a17f2855cc12ad36fd614c590b9d18f46dfd65d
Provides: bundled(golang(github.com/casbin/casbin/util)) = 3a17f2855cc12ad36fd614c590b9d18f46dfd65d
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
Provides: bundled(golang(github.com/go-test/deep)) = 57af0be209c537ba1d9c2a4b285ab7aea0897e51
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
Provides: bundled(golang(github.com/golang/protobuf/protoc-gen-go)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/protoc-gen-go/descriptor)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/protoc-gen-go/generator)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/protoc-gen-go/grpc)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/protoc-gen-go/plugin)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/ptypes)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/ptypes/any)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/ptypes/duration)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/golang/protobuf/ptypes/struct)) = bbd03ef6da3a115852eaf24c8a1c46aeb39aa175
Provides: bundled(golang(github.com/golang/protobuf/ptypes/timestamp)) = 925541529c1fa6821df4e44ce2723319eb2be768
Provides: bundled(golang(github.com/google/btree)) = cc6329d4279e3f025a53a83c397d2339b5705c45
Provides: bundled(golang(github.com/google/gofuzz)) = 24818f796faf91cd76ec7bddd72458fbced7a6c1
Provides: bundled(golang(github.com/google/gopacket)) = 67a21c4470a0598531a769727aef40b870ffa128
Provides: bundled(golang(github.com/google/gopacket/ip4defrag)) = 67a21c4470a0598531a769727aef40b870ffa128
Provides: bundled(golang(github.com/google/gopacket/layers)) = 67a21c4470a0598531a769727aef40b870ffa128
Provides: bundled(golang(github.com/google/gopacket/pcap)) = 67a21c4470a0598531a769727aef40b870ffa128
Provides: bundled(golang(github.com/google/gopacket/pcapgo)) = 67a21c4470a0598531a769727aef40b870ffa128
Provides: bundled(golang(github.com/google/gopacket/tcpassembly)) = 67a21c4470a0598531a769727aef40b870ffa128
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
Provides: bundled(golang(github.com/hashicorp/go-version)) = 23480c0665776210b5fbbac6eaaee40e3e6a96b7
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
Provides: bundled(golang(github.com/jteeuwen/go-bindata)) = 6025e8de665b31fa74ab1a66f2cddd8c0abf887e
Provides: bundled(golang(github.com/jteeuwen/go-bindata/go-bindata)) = 6025e8de665b31fa74ab1a66f2cddd8c0abf887e
Provides: bundled(golang(github.com/juju/loggo)) = 8232ab8918d91c72af1a9fb94d3edbe31d88b790
Provides: bundled(golang(github.com/juju/ratelimit)) = 5b9ff866471762aa2ab2dced63c9fb6f53921342
Provides: bundled(golang(github.com/juju/webbrowser)) = 54b8c57083b4afb7dc75da7f13e2967b2606a507
Provides: bundled(golang(github.com/julienschmidt/httprouter)) = d1898390779332322e6b5ca5011da4bf249bb056
Provides: bundled(golang(github.com/kami-zh/go-capturer)) = e492ea43421da7381e5200a2e22753bfc31347c2
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
Provides: bundled(golang(github.com/mailru/easyjson)) = 8b799c424f57fa123fc63a99d6383bc6e4c02578
Provides: bundled(golang(github.com/mailru/easyjson/bootstrap)) = 3fdea8d05856a0c8df22ed4bc71b3219245e4485
Provides: bundled(golang(github.com/mailru/easyjson/buffer)) = 2a92e673c9a6302dd05c3a691ae1f24aef46457d
Provides: bundled(golang(github.com/mailru/easyjson/easyjson)) = 3fdea8d05856a0c8df22ed4bc71b3219245e4485
Provides: bundled(golang(github.com/mailru/easyjson/gen)) = 3fdea8d05856a0c8df22ed4bc71b3219245e4485
Provides: bundled(golang(github.com/mailru/easyjson/jlexer)) = 2a92e673c9a6302dd05c3a691ae1f24aef46457d
Provides: bundled(golang(github.com/mailru/easyjson/jwriter)) = 2a92e673c9a6302dd05c3a691ae1f24aef46457d
Provides: bundled(golang(github.com/mailru/easyjson/parser)) = 3fdea8d05856a0c8df22ed4bc71b3219245e4485
Provides: bundled(golang(github.com/mattn/go-runewidth)) = d6bea18f789704b5f83375793155289da36a3c7f
Provides: bundled(golang(github.com/matttproud/golang_protobuf_extensions/pbutil)) = d0c3fe89de86839aecf2e0579c40ba3bb336a453
Provides: bundled(golang(github.com/mitchellh/go-homedir)) = 756f7b183b7ab78acdbbee5c7f392838ed459dda
Provides: bundled(golang(github.com/mitchellh/hashstructure)) = ab25296c0f51f1022f01cd99dfb45f1775de8799
Provides: bundled(golang(github.com/mitchellh/mapstructure)) = 281073eb9eb092240d33ef253c404f1cca550309
Provides: bundled(golang(github.com/mohae/deepcopy)) = c48cc78d482608239f6c4c92a4abd87eb8761c90
Provides: bundled(golang(github.com/nlewo/contrail-introspect-cli/collection)) = e4df28ccf9801abbe32edd5ddaba31a7a62b61b6
Provides: bundled(golang(github.com/nlewo/contrail-introspect-cli/descriptions)) = e4df28ccf9801abbe32edd5ddaba31a7a62b61b6
Provides: bundled(golang(github.com/nlewo/contrail-introspect-cli/utils)) = e4df28ccf9801abbe32edd5ddaba31a7a62b61b6
Provides: bundled(golang(github.com/nu7hatch/gouuid)) = 179d4d0c4d8d407a32af483c2354df1d2c91e6c3
Provides: bundled(golang(github.com/olivere/elastic)) = 4eb0cace57d54aa19e2c709e13979daeb20130a6
Provides: bundled(golang(github.com/olivere/elastic/config)) = 4eb0cace57d54aa19e2c709e13979daeb20130a6
Provides: bundled(golang(github.com/olivere/elastic/uritemplates)) = 4eb0cace57d54aa19e2c709e13979daeb20130a6
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
Provides: bundled(golang(github.com/safchain/ethtool)) = 6e3f4faa84e1d8d48afec75ed064cf3611d3f8bf
Provides: bundled(golang(github.com/safchain/insanelock)) = 33bca45866480bc4b8caca2a94898c3baf161c1e
Provides: bundled(golang(github.com/shirou/gopsutil/cpu)) = 6a368fb7cd1221fa6ea90facc9447c9a2234c255
Provides: bundled(golang(github.com/shirou/gopsutil/host)) = 6a368fb7cd1221fa6ea90facc9447c9a2234c255
Provides: bundled(golang(github.com/shirou/gopsutil/internal/common)) = 6a368fb7cd1221fa6ea90facc9447c9a2234c255
Provides: bundled(golang(github.com/shirou/gopsutil/mem)) = 6a368fb7cd1221fa6ea90facc9447c9a2234c255
Provides: bundled(golang(github.com/shirou/gopsutil/net)) = 6a368fb7cd1221fa6ea90facc9447c9a2234c255
Provides: bundled(golang(github.com/shirou/gopsutil/process)) = 6a368fb7cd1221fa6ea90facc9447c9a2234c255
Provides: bundled(golang(github.com/shirou/w32)) = bb4de0191aa41b5507caa14b0650cdbddcd9280b
Provides: bundled(golang(github.com/skydive-project/dede/dede)) = 90df8e39b679fe75c1f2e8c3d9f3dd4646b9771f
Provides: bundled(golang(github.com/skydive-project/dede/statics)) = 90df8e39b679fe75c1f2e8c3d9f3dd4646b9771f
Provides: bundled(golang(github.com/socketplane/libovsdb)) = 5113f8fb4d9d374417ab4ce35424fbea1aad7272
Provides: bundled(golang(github.com/spaolacci/murmur3)) = f09979ecbc725b9e6d41a297405f65e7e8804acc
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
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = 1d523034197ff1f222f6429836dd36a2457a1874
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
Provides: bundled(golang(k8s.io/api/admissionregistration/v1alpha1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/admissionregistration/v1beta1)) = kubernetes-1.9.1
Provides: bundled(golang(k8s.io/api/apps/v1)) = kubernetes-1.9.1
Provides: bundled(golang(k8s.io/api/apps/v1beta1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/apps/v1beta2)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/authentication/v1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/authentication/v1beta1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/authorization/v1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/authorization/v1beta1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/autoscaling/v1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/autoscaling/v2beta1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/batch/v1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/batch/v1beta1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/batch/v2alpha1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/certificates/v1beta1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/core/v1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/events/v1beta1)) = kubernetes-1.9.1
Provides: bundled(golang(k8s.io/api/extensions/v1beta1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/networking/v1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/policy/v1beta1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/rbac/v1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/rbac/v1alpha1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/rbac/v1beta1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/scheduling/v1alpha1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/settings/v1alpha1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/storage/v1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/api/storage/v1alpha1)) = kubernetes-1.9.1
Provides: bundled(golang(k8s.io/api/storage/v1beta1)) = 006a217681ae70cbacdd66a5e2fca1a61a8ff28e
Provides: bundled(golang(k8s.io/apimachinery/pkg/api/errors)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/api/meta)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/api/resource)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/internalversion)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/v1)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/v1alpha1)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/conversion)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/conversion/queryparams)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/fields)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/labels)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/schema)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/json)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/protobuf)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/recognizer)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/streaming)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/versioning)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/selection)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/types)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/cache)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/clock)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/diff)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/errors)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/framer)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/intstr)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/json)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/net)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/runtime)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/sets)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/validation)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/validation/field)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/wait)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/yaml)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/version)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/pkg/watch)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/apimachinery/third_party/forked/golang/reflect)) = 68f9c3a1feb3140df59c67ced62d3a5df8e6c9c2
Provides: bundled(golang(k8s.io/client-go/discovery)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/scheme)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/admissionregistration/v1alpha1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/admissionregistration/v1beta1)) = kubernetes-1.9.1
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/apps/v1)) = kubernetes-1.9.1
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/apps/v1beta1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/apps/v1beta2)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authentication/v1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authentication/v1beta1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authorization/v1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authorization/v1beta1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/autoscaling/v1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/autoscaling/v2beta1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/batch/v1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/batch/v1beta1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/batch/v2alpha1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/certificates/v1beta1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/core/v1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/events/v1beta1)) = kubernetes-1.9.1
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/extensions/v1beta1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/networking/v1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/policy/v1beta1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/rbac/v1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/rbac/v1alpha1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/rbac/v1beta1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/scheduling/v1alpha1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/settings/v1alpha1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/storage/v1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/storage/v1alpha1)) = kubernetes-1.9.1
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/storage/v1beta1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/pkg/version)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/rest)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/rest/watch)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/tools/auth)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/tools/cache)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/tools/clientcmd)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/tools/clientcmd/api)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/tools/clientcmd/api/latest)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/tools/clientcmd/api/v1)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/tools/metrics)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/tools/pager)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/tools/reference)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/transport)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/util/buffer)) = kubernetes-1.9.1
Provides: bundled(golang(k8s.io/client-go/util/cert)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/util/flowcontrol)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/util/homedir)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/client-go/util/integer)) = 9389c055a838d4f208b699b3c7c51b70f2368861
Provides: bundled(golang(k8s.io/kube-openapi/pkg/common)) = 39a7bf85c140f972372c2a0d1ee40adbf0c8bfe1

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
Requires(post):   systemd %{selinux_semanage_pkg}
Requires(preun):  systemd
Requires(postun): systemd %{selinux_semanage_pkg}

%description analyzer
Collects data captured by the Skydive agents.

%package agent
Summary:          Skydive agent
Requires:         %{name} = %{version}-%{release}
Requires(post):   systemd %{selinux_semanage_pkg}
Requires(preun):  systemd
Requires(postun): systemd %{selinux_semanage_pkg}

%description agent
The Skydive agent has to be started on each node where the topology and
flows informations will be captured.

%package ansible
Summary:          Skydive ansible recipes
Requires:         %{name} = %{version}-%{release}
Requires:         ansible

%description ansible
Ansible recipes to deploy Skydive

%package selinux
Summary:          Skydive selinux recipes
Requires:         container-selinux, policycoreutils, libselinux-utils
Requires(post):   selinux-policy-base >= %{selinux_policyver}, policycoreutils
Requires(postun): policycoreutils
BuildArch:        noarch

%description selinux
This package installs and sets up the SELinux policy security module for Skydive.

%prep
%setup -q -n skydive-%{fullver}/src/%{import_path}

%build
export GOPATH=%{_builddir}/skydive-%{fullver}
make compile BUILD_CMD=go VERSION=%{fullver} %{with_features}
%{_builddir}/skydive-%{fullver}/bin/skydive bash-completion

# SELinux build
%if 0%{?fedora} >= 27
cp contrib/packaging/rpm/skydive.te{.fedora,}
%endif
%if 0%{?rhel} >= 7
cp contrib/packaging/rpm/skydive.te{.rhel,}
%endif
make -f /usr/share/selinux/devel/Makefile -C contrib/packaging/rpm/ skydive.pp
bzip2 contrib/packaging/rpm/skydive.pp

%install
install -D -p -m 755 %{_builddir}/skydive-%{fullver}/bin/skydive %{buildroot}%{_bindir}/skydive
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

# SELinux
install -D -m 644 contrib/packaging/rpm/skydive.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/skydive.pp.bz2
install -D -m 644 contrib/packaging/rpm/skydive.if %{buildroot}%{_datadir}/selinux/devel/include/contrib/skydive.if
install -D -m 644 contrib/packaging/rpm/skydive-selinux.8 %{buildroot}%{_mandir}/man8/skydive-selinux.8

%post agent
if %{_sbindir}/selinuxenabled && [ "$1" = "1" ] ; then
    set +e
    %{_sbindir}/semanage port -a -t skydive_agent_sflow_ports_t -p udp 6343
    %{_sbindir}/semanage port -a -t skydive_agent_sflow_ports_t -p udp 6345-6355
    %{_sbindir}/semanage port -a -t skydive_agent_pcapsocket_ports_t -p tcp 8100-8132
fi
%systemd_post %{basename:%{name}-agent.service}

%preun agent
%systemd_preun %{basename:%{name}-agent.service}

%postun agent
%systemd_postun
if %{_sbindir}/selinuxenabled && [ "$1" = "0" ] ; then
    set +e
    %{_sbindir}/semanage port -d -t skydive_agent_sflow_ports_t -p udp 6343
    %{_sbindir}/semanage port -d -t skydive_agent_sflow_ports_t -p udp 6345-6355
    %{_sbindir}/semanage port -d -t skydive_agent_pcapsocket_ports_t -p tcp 8100-8132
fi

%post analyzer
if %{_sbindir}/selinuxenabled && [ "$1" = "1" ] ; then
    set +e
    %{_sbindir}/semanage port -a -t skydive_etcd_ports_t -p tcp 12379-12380
    %{_sbindir}/semanage port -a -t skydive_analyzer_db_connect_ports_t -p tcp 2480
    %{_sbindir}/semanage port -a -t skydive_analyzer_db_connect_ports_t -p tcp 9200
fi
%systemd_post %{basename:%{name}-analyzer.service}

%preun analyzer
%systemd_preun %{basename:%{name}-analyzer.service}

%postun analyzer
%systemd_postun
if %{_sbindir}/selinuxenabled && [ "$1" = "0" ] ; then
    set +e
    %{_sbindir}/semanage port -d -t skydive_etcd_ports_t -p tcp 12379-12380
    %{_sbindir}/semanage port -d -t skydive_analyzer_db_connect_ports_t -p tcp 2480
    %{_sbindir}/semanage port -d -t skydive_analyzer_db_connect_ports_t -p tcp 9200
fi

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{name}.pp.bz2

%postun selinux
if [ "$1" = "0" ]; then
    %selinux_modules_uninstall -s %{name}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%check
%{buildroot}%{_bindir}/skydive version | grep -q "skydive github.com/skydive-project/skydive %{fullver}" || exit 1

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

%files selinux
%attr(0644,root,root) %{_datadir}/selinux/packages/%{name}.pp.bz2
%attr(0644,root,root) %{_datadir}/selinux/devel/include/%{moduletype}/%{name}.if
%attr(0644,root,root) %{_mandir}/man8/skydive-selinux.8.*

%changelog
* Wed Aug 8 2018 Sylvain Baubeau <sbaubeau@redhat.com> - 0.19.0-1
- Bump to version 0.19.0

* Mon Jun 18 2018 Sylvain Baubeau <sbaubeau@redhat.com> - 0.18.0-1
- Bump to version 0.18.0
- Add SElinux policy

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

