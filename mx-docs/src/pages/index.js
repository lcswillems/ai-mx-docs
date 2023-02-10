import React from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import HomepageFeatures from "@site/src/components/HomepageFeatures";

export default function Home() {
  return (
    <Layout
      title="Docs"
      description="A highly scalable, fast and secure blockchain platform for distributed apps, enterprise use cases and the new internet economy."
    >
      <HomepageFeatures />
    </Layout>
  );
}
