export default function loadBalancer(chinaDownload, USDownload) {
  const value = Promise.any([chinaDownload, USDownload]);
  return value;
}
