# Issue 67 hosted CI fixture

Private, isolated synthetic acceptance repository. No application code, deployment,
environments or repository secrets. Pushes run three Python unittest cases on a
GitHub-hosted runner with read-only contents permission. Checkout is pinned by SHA
and does not persist credentials. Test counts and the exact pushed SHA are emitted
as a check annotation consumed by agent-platform's hosted evidence adapter.

This is environment preparation, not a genuine Tim/Ryan request or an end-to-end
acceptance pass. No application repository is enrolled by this setup.
