---
id: real-input-e-holds
title: The real branching input holds
kind: theorem
decl: UpperTheory.Lit.realInputE_holds
module: Development.AutomorphicArithmetic.ThetaCorrespondence.FockModels.RealBranch
covers: 942
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{RealInputE}$, an archimedean input about discrete series of indefinite unitary groups. It is the fourth input of [real functionals separate](/proof/bessel-seesaw/), which [functionals separate from Howe and Siegel-Weil](/proof/bessel-seesaw/) uses. There it gives the bottom period $P_0 \neq 0$ through [the cusp form with a nonzero theta period](/proof/siegel-weil/). The proof only feeds two proved facts into one lemma.

## Statement

Take $n \geq 3$, signs $\varepsilon$ on $n+1$ coordinates and $\varepsilon'$ on $n$ coordinates, and Harish-Chandra parameters $\lambda$, $\mu$ that interlace, with gaps of at least 2 and at least $1000(n+1)^3$ between opposite signs, and with all entries at most $B$ in size. Let $\pi$ and $\sigma$ be discrete series of $U(J_\varepsilon) \subset \mathrm{GL}_{n+1}(\mathbb{C})$ and $U(J_{\varepsilon'})$ with these parameters. Embed $U(J_{\varepsilon'})$ in $U(J_\varepsilon)$ by a 1 in one slot $e_0$. Put $\mathrm{big}(C,n,B) = \exp(C(n+1)^4 \log(8(n+1)B))$.

**Theorem.** There is $C > 0$ such that for each such pair there are a unit $v_0$ in the lowest $K$-type of $\pi$, $g_0 \in U(J_\varepsilon)$, a smooth unit vector $w'$ of $\sigma$ and $c > 0$ with $v = \pi(g_0)v_0$ and:

1. $\int \overline{\langle v, \pi(h)v\rangle}\,\langle b, \sigma(h)w'\rangle\,dh = c\,\langle b, w'\rangle$ for each $b$;
2. $\int |\langle v, \pi(gh)v\rangle|\,dh \leq c\,\mathrm{big}(C,n,B)\,|g e_0|^{-(2n+7)}$ for $g \in U(J_\varepsilon)$;
3. the same integral with $d\pi(X)v$ in the first slot is at most $c\,\mathrm{big}(C,n,B)$ when $X$ is in the Lie algebra of $U(J_{\varepsilon'})$ with Hilbert-Schmidt norm at most 1;
4. $|\langle v, \pi(g)v\rangle| \leq A\,\|g\|^{-20(n+1)^2}$ for some $A$.

All integrals are over $h \in U(J_{\varepsilon'})$.

## Proof

The proof is one application of `Branch.realInputE`, which takes two facts. `ProjLarge`, proved by `projLarge_of` from `seedB_of` and `bigProjP`, gives $g_0$ with $\|g_0\|$ bounded and $\|P\pi(g_0)v_0\| \geq 1/\mathrm{big}$, where $P$ projects to a copy of $\sigma$. `EigMap`, proved by `eigMap_of` from `eigA` and `tMap`, turns a vector with a large projection into a $w$ that satisfies item 1. `Branch.realInputE` adds the bounds of items 2 and 3 from general integral estimates and normalizes $w$. The rest is bookkeeping.

## In the Lean code

The theorem is in [RealBranch.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/FockModels/RealBranch.lean#L231). $\mathrm{RealInputE}$ is in [BranchDefs.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/RealBands/BranchDefs.lean#L11), the lemma in [BranchInput.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/RealBands/BranchInput.lean#L41).

Item 1 in Lean reads $c\,\langle w', w'\rangle\langle b, w'\rangle$. The factor $\langle w', w'\rangle$ is 1. The stronger form `RealInput` in [ProjExists.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/ProjExists.lean#L102) has $\langle w', a\rangle$ for each $a$. A second user, `functionalsSeparate_free`, is at line 237.
