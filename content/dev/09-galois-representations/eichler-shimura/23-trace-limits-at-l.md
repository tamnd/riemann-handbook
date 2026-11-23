---
title: Trace limits at the residue characteristic
decls:
  - UpperTheory.Gal.ClosedPhiFromClosedTrace.ClosedTr_holds
  - UpperTheory.Gal.ClosedPhiFromClosedTrace.congPhi_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Trace limits at the residue characteristic

The Galois representations of the main line are made as limits. A representation $r$ is known only through its traces, and these traces are limits of linear combinations of traces of representations $\rho$ that come from geometry. At a place $w$ above $\ell$, the local data of $r$ at $w$ is its Weil-Deligne representation, and this data is not a continuous function of the traces in a simple sense. This section proves that, under a bound on the Hodge-Tate jumps, the traces of the Weil-Deligne representation at $w$ do pass to the limit. The main result is [Theorem 3.24.7](/entry/closed-tr-holds/). Its form for power sums of Frobenius eigenvalues is [Theorem 3.24.8](/entry/cong-phi-holds/), and [the main line](/entry/core-all-of/) gives this form to the core statement of Section 26.

We keep the notation of Section 03 and Section 18. $E$ is a number field, $\Omega$ an algebraic closure of $E$ and $G_E = \mathrm{Gal}(\Omega/E)$. We fix a prime $\ell$, an isomorphism $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$ and a system of period rings over $\mathbb{Q}_\ell$ with $A_{\inf}$, $A_{\mathrm{cris}} \subset B_{\mathrm{cris}}$ and $B_{\mathrm{st}}$, compatible with each other. Let $w$ be a finite place of $E$, $A$ a valuation ring of $\Omega$ over $w$, $D_A \subset G_E$ its decomposition group and $W_A \subset D_A$ its Weil group. A *local bridge* at $A$ is an identification of $D_A$ with the absolute Galois group of a finite extension $K_w$ of $\mathbb{Q}_\ell$, together with the embeddings of $E$ that it induces. For a continuous $r : G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$ that is potentially semistable at $w$, we write $\mathrm{WD}_w(r)$ for its Weil-Deligne representation, made complex by $\iota$, as in Section 03. The words *semistable at $w$*, *crystalline at $w$* and *jumps $J(\tau)$ at $\tau$* refer to the restriction of $r$ to $D_A$ through the bridge. A *jump function* $J$ assigns to each embedding $\tau : E \to \overline{\mathbb{Q}}_\ell$ a finite multiset of integers.

### Approximation of traces

**Definition 3.24.1 (Joint trace approximation).** Let $k$ be a normed field, $\Gamma$ a group, $r : \Gamma \to \mathrm{GL}_a(k)$ a representation and $C$ a set of representations $\Gamma \to \mathrm{GL}_a(k)$.

1. Let $p$ be a function from representations to $k$ and let $\theta \in k$. We say that *$C$ approximates $r$ jointly with $p$ to $\theta$* if for each $\varepsilon > 0$ there are a finite set $s \subset C$ and coefficients $c_\rho \in k$ such that $\lVert \mathrm{tr}\, r(g) - \sum_{\rho \in s} c_\rho\, \mathrm{tr}\, \rho(g) \rVert \leq \varepsilon$ for every $g \in \Gamma$ and $\lVert \theta - \sum_{\rho \in s} c_\rho\, p(\rho) \rVert \leq \varepsilon$.
2. Let $S : \mathbb{N} \to k$ and let $p(\rho, j)$ be a function of a representation and an index. We say that *$C$ approximates $r$ jointly with $p$ to $S$* if for each $n$ and each $\varepsilon > 0$ there are $s$ and $c$ as in 1 with the trace bound and with $\lVert S(j) - \sum_{\rho \in s} c_\rho\, p(\rho, j) \rVert \leq \varepsilon$ for all $j \leq n$.

Lean: `UpperTheory.Gal.ClosedPhiFromClosedTrace.JointApprox` (also `GlobalTheory.CongPhi.JointApprox`).

The trace bound alone is *trace approximation* of $r$ by $C$. The extra value $p$ is a quantity that we want to follow to the limit, with the same finite combinations that approximate the traces.

**Definition 3.24.2 (Weil-Deligne traces and Frobenius power sums).** Let $r$ be a representation of $D_A$ and $g \in W_A$. The *Weil-Deligne trace* $\mathrm{wdTr}(r, g) \in \overline{\mathbb{Q}}_\ell$ is $\iota^{-1}(-c)$, where $c$ is the coefficient of $X^{a-1}$ in the characteristic polynomial of $g$ on $\mathrm{WD}_w(r)$. For a Weil-Deligne representation $x$ at $w$, an element $\sigma \in W_A$ and $n \in \mathbb{N}$, the *Frobenius power sum* $\phi_n(x, \sigma) \in \mathbb{C}$ is the sum of $\alpha^n$ over the roots $\alpha$ of the characteristic polynomial of $\sigma$ on $x$, counted with multiplicity.

Lean: `UpperTheory.Gal.ClosedPhiFromClosedTrace.wdTr` (also `GlobalTheory.CongPhi.phiSum`).

The characteristic polynomial is monic and splits over $\mathbb{C}$, so $-c$ is the sum of its roots. Thus $\mathrm{wdTr}(r, g)$ is $\iota^{-1}$ of the trace of $g$ on $\mathrm{WD}_w(r)$, and $\phi_1(x, \sigma)$ is the trace of $\sigma$ on $x$.

**Lemma 3.24.3 (Power sums are traces).** For every Weil-Deligne representation $x$ at $w$, every $\sigma \in W_A$ and every $n$, $\phi_n(x, \sigma)$ is the trace of $\sigma^n$ on $x$.

Lean: `UpperTheory.Gal.ClosedPhiFromClosedTrace.powTr_holds` (also `UpperTheory.Gal.ClosedPhiFromClosedTrace.PowTr`).

*Proof.* The roots of the characteristic polynomial of $\sigma^n$ are the $n$-th powers of the roots of the characteristic polynomial of $\sigma$, with multiplicities. For a monic polynomial that splits, minus the coefficient of the second highest power is the sum of the roots. $\square$

### The two closure statements

**Definition 3.24.4 (Closed trace statement).** The *closed trace statement* is the following claim. Let $E, \Omega, \ell, \iota$ be as above, $a \geq 1$, $w$ a finite place, $A$ over $w$ with a local bridge, and $J$ a jump function. Let $r : G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$ be continuous and semisimple, let $C$ be a set of representations of $G_E$ of dimension $a$, let $g \in W_A$ and $\theta \in \overline{\mathbb{Q}}_\ell$. Assume that every $\rho \in C$ is continuous, semistable at $w$, crystalline at $w$ and has jumps $J(\tau)$ at every $\tau$. Assume that $C$ approximates $r$ jointly with $\rho \mapsto \mathrm{wdTr}(\rho, g)$ to $\theta$. Then $\mathrm{wdTr}(r, g) = \theta$.

Lean: `UpperTheory.Gal.ClosedPhiFromClosedTrace.ClosedTr`.

**Definition 3.24.5 (Closed Frobenius statement).** The *closed Frobenius statement* is the following claim. Let the data $E, \Omega, \ell, \iota, a, w, A, J, r$ and $C$ be as in the closed trace statement, and assume that every $\rho \in C$ is continuous, crystalline at $w$ and has jumps $J(\tau)$ at every $\tau$. Let $\sigma \in W_A$ and $S : \mathbb{N} \to \overline{\mathbb{Q}}_\ell$, and assume that $C$ approximates $r$ jointly with $(\rho, n) \mapsto \iota^{-1}\phi_n(\mathrm{WD}_w(\rho), \sigma)$ to $S$. Then $\phi_n(\mathrm{WD}_w(r), \sigma) = \iota(S(n))$ for every $n$.

Lean: `GlobalTheory.CongPhi.ClosedPhi`.

In the main line, $C$ is a set of representations that come from geometry and $r$ is a limit of them in the sense of traces. The closed Frobenius statement then gives the Frobenius eigenvalues of $\mathrm{WD}_w(r)$ at a place above $\ell$ from those of the members of $C$. The fixed jump function $J$ is the essential hypothesis. Without a bound on the jumps, a trace limit of crystalline representations need not be de Rham.

### Integral covers

The proof of the closed trace statement replaces trace approximation by an integral structure. We describe it in words.

**Definition 3.24.6 (Integral cover).** Let $\Gamma$ be a topological group, $L_0$ a finite extension of $\mathbb{Q}_\ell$, $r : \Gamma \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$ and $C$ a set of representations. An integral representation $\rho : \Gamma \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ *reads* $r$ through matrices $b_1, \dots, b_d \in M_a(\overline{\mathbb{Q}}_\ell)$ and $e \in \mathbb{Z}_\ell^d$ if $r(g) b_j = \sum_i \rho(g)_{ij} b_i$ for all $g, j$ and $\sum_i e_i b_i = 1$. An *integral cover* of $r$ by $C$ consists of:

1. a continuous $\rho$ that reads $r$ through $b$ and $e$;
2. a tower of continuous integral representations $\rho'_m$ of $\Gamma$ with matrices $\Pi_m$ that intertwine $\rho'_m$ with $\rho$ modulo $\ell^m$ and are onto modulo $\ell^m$, and with transition maps between $\rho'_{m+1}$ and $\rho'_m$ that are compatible with the $\Pi_m$ modulo $\ell^m$;
3. for each $m$ a *layer*: finitely many members $\rho_{m,1}, \dots, \rho_{m,k_m}$ of $C$ with coefficient fields that contain $L_0$, a basis of their joint matrix span on which $\rho'_m$ reads them, a vector $e_m$ with $\Pi_m e_m \equiv e$ modulo $\ell^m$, and coefficients $c_{m,k}$;

such that at each layer $m$ the traces of the reading of $r$ through $\Pi_m$ differ from $\sum_k c_{m,k}$ times the traces of the readings of $\rho_{m,k}$ by at most $\ell^{-m}$.

Lean: `GlobalTheory.BKLim.Cover` (also `GlobalTheory.BKLim.Reads`, `GlobalTheory.BKLim.Tower`, `GlobalTheory.BKLim.Layer`).

The first condition says that the $\mathbb{Z}_\ell$-span of the image of $r$ is a lattice on which $\Gamma$ acts by left multiplication. Since $\sum_i e_i b_i = 1$, the trace of $r(g)$ is a fixed linear function of the matrix $\rho(g)$. Thus traces of $r$ become entries of an integral representation, which can be compared with integral period matrices.

### The closed trace theorem

**Theorem 3.24.7 (Closed trace).** The closed trace statement holds.

Lean: `UpperTheory.Gal.ClosedPhiFromClosedTrace.ClosedTr_holds` (also `UpperTheory.Gal.ClosedPhiFromClosedTrace.closedTr_of`).

*Proof.* Fix the data. The proof has seven steps. Each step uses one of the integral period lemmas that are named in the Remark below, and we give their content in outline.

1. *The limit is crystalline.* The trace part of the joint approximation says that $C$ approximates $r$ in traces. The members of $C$ are continuous and semistable at $w$ and have the fixed jumps $J$. By the closedness theorem for trace limits with fixed jumps, $r$ is de Rham at $w$ with jumps $J$. The same theorem says that if every member of $C$ is crystalline at $w$, then so is $r$. So $r$ is crystalline at $w$.
2. *An integral cover with control of $\theta$.* Since $r$ is continuous and semisimple and $D_A$ is compact, there is an integral cover of $r$ restricted to $D_A$ by the restrictions of the members of $C$. The cover can be chosen so that, at each layer $m$, $\lVert \theta - \sum_k c_{m,k}\,\mathrm{wdTr}(\rho_{m,k}, g) \rVert \leq \ell^{-m}$, with the coefficients $c_{m,k}$ of that layer.
3. *Breuil-Kisin frames.* Choose a Breuil-Kisin datum for $K_w$ and a period element for it. Each member of $C$ is semistable with jumps $J$, and crystalline. From these facts one gets a height $N$, frames $F_0$ for $\rho$ and $F_m$ for each $\rho'_m$, all of crystalline type, and an integer $r_0$ such that for each $n$ there is $m \geq n$ with $F_0$ and $F_m$ linked through $\Pi_m$ modulo $\ell^n$ with defect $\ell^{r_0}$.
4. *Frobenius on the residue field.* Let $\alpha(g) \in \mathbb{Z}$ be the residue degree of $w$ times the degree of $g$. Then the $\lvert \alpha(g) \rvert$-th power of the Frobenius of the maximal unramified extension of $\mathbb{Q}_\ell$ fixes every unramified element of $K_w$. Write $\alpha(g) = n_2 - n_1$ with $n_1 = \max(-\alpha(g), 0)$ and $n_2 = \max(\alpha(g), 0)$.
5. *Operators on periods.* From the frames one gets a scalar $s$ that is a unit in $B_{\mathrm{cris}}$, a matrix $V$ for $\rho$ and matrices $V_m$ for $\rho'_m$, with entries in $A_{\mathrm{cris}}$. Each of them satisfies $V\, \varphi^{n_2}(U) = s\, \varphi^{n_1}(U)$ for an invertible period matrix $U$ of the integral representation, where $\varphi$ is the Frobenius of $B_{\mathrm{cris}}$. For each $M$ there is $m \geq M$ with $V \Pi_m \equiv \Pi_m V_m$ modulo $\ell^M$.
6. *Operators give traces.* For a representation that is crystalline at $w$ and read by an integral representation with such an operator, a linear identity in $B_{\mathrm{cris}}$ ties the operator to $\mathrm{wdTr}(\cdot, g)$. This applies to $r$ by step 1, and to each $\rho_{m,k}$ since it is crystalline.
7. *Passage to the limit.* The identities of step 6 for $r$ and for the layers, the congruences of step 5 and the bounds of step 2 give $\mathrm{wdTr}(r, g) = \theta$.

This gives the claim. $\square$

Step 1 is where the fixed jumps are used. Steps 3 to 7 then make the Frobenius of $\mathrm{WD}_w(r)$ at $g$ a limit, in the $\ell$-adic topology of $A_{\mathrm{cris}}$, of the Frobenius data of the layers. The degree $\alpha(g)$ can have either sign, and this is the reason for the two exponents $n_1$ and $n_2$ in step 5.

### Power sums of Frobenius eigenvalues

**Theorem 3.24.8 (Closed Frobenius).** The closed Frobenius statement holds.

Lean: `UpperTheory.Gal.ClosedPhiFromClosedTrace.congPhi_holds` (also `UpperTheory.Gal.ClosedPhiFromClosedTrace.congPhi_of_closedTr`).

*Proof.* Fix the data and $n$. We apply [Theorem 3.24.7](/entry/closed-tr-holds/) with $g = \sigma^n$ and $\theta = S(n)$.

First, the members of $C$ satisfy the hypotheses of the closed trace statement. Each $\rho \in C$ is crystalline at $w$, and a crystalline representation is semistable. The other conditions are the same.

Second, $C$ approximates $r$ jointly with $\rho \mapsto \mathrm{wdTr}(\rho, \sigma^n)$ to $S(n)$. Let $\varepsilon > 0$. The joint approximation to $S$, at the index $n$, gives a finite $s \subset C$ and coefficients $c$ with the trace bound and with $\lVert S(j) - \sum_{\rho \in s} c_\rho\, \iota^{-1}\phi_j(\mathrm{WD}_w(\rho), \sigma) \rVert \leq \varepsilon$ for all $j \leq n$. Take $j = n$. By the lemma that power sums are traces, $\iota^{-1}\phi_n(\mathrm{WD}_w(\rho), \sigma) = \mathrm{wdTr}(\rho, \sigma^n)$. This is the required bound.

So the theorem gives $\mathrm{wdTr}(r, \sigma^n) = S(n)$. Apply $\iota$ and the lemma again: $\phi_n(\mathrm{WD}_w(r), \sigma) = \iota(\mathrm{wdTr}(r, \sigma^n)) = \iota(S(n))$. $\square$

The proof uses only the index $j = n$ of the joint approximation. The uniform control of all $j \leq n$ by one finite combination is not necessary for this theorem.

**Remark 3.24.9 (Formalization).** The two theorems are in [ClosedPhiHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ClosedPhiFunctoriality/ClosedPhiHolds.lean#L36), at lines 36 and 44. The reductions `closedTr_of` and `congPhi_of_closedTr` are in [ClosedPhiOfClosedTr.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ClosedPhiFunctoriality/ClosedPhiOfClosedTr.lean#L13), and we read both in full. `ClosedTr` and `PowTr` are in [IsOp2One.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ClosedPhiFunctoriality/IsOp2One.lean#L91), and `ClosedPhi` with `phiSum` is in [JointApproxOfMem.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/JointApproxOfMem.lean#L79). The degree $\alpha(g)$ is `alpha` in [FiniteDimensionalLetter.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/FiniteDimensionalLetter.lean#L140). We did not open the proofs of the step lemmas: `GlobalTheory.LimitTop.closedAtL` (step 1), `coverJ_holds` (step 2), `frEx_holds` (step 3), `fixOf_holds` (step 4), `opEx_holds` with its inputs `secU_holds`, `coreU_holds`, `invQ_holds`, `invU_holds`, `linkZ_holds`, `linkA_holds`, `linkQ_holds`, `zeroAp_holds`, `linkRec_holds`, `linkOp_holds`, `fixW_holds` and `opOne_holds` (step 5), `tie_holds` with `tieRep_holds`, `trLin_holds`, `coordEx_holds`, `coordWD_holds`, `colInv_holds`, `weilPhi_holds` and `testTr_holds` (step 6), and `trLim_holds` with `trStep_holds`, `func_holds`, `intBasis_holds` and `trId_holds` (step 7). We also did not open `GlobalTheory.AboveL.eig_pow_of_rep`, used in the lemma on power sums, or `GlobalTheory.CrysSst.isSstAt_of_isCrysAt`. Three things are odd. First, `ClosedTr` asks the members of $C$ to be both semistable and crystalline at $w$ ([IsOp2One.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ClosedPhiFunctoriality/IsOp2One.lean#L99)), and the first condition follows from the second. Second, the local [JointApproxOfMem.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ClosedPhiFunctoriality/JointApproxOfMem.lean#L34) defines another `ClosedPhi` in the namespace `UpperTheory.Gal.ClosedPhiFromClosedTrace`, with the extra hypothesis $\deg g \leq 0$; it is not used by the theorems here. The same file defines a `JointApprox` (line 16) that has the same name as the sequence version in the other `JointApproxOfMem.lean` (line 18). Third, the proof of `closedAtL` builds its own integral cover, and `closedTr_of` then builds a second one through `CoverJ`.
