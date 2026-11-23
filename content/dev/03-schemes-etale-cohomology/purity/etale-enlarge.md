---
id: etale-enlarge
title: Roots of uniformisers make the closure of a torsor étale in codimension one
kind: theorem
decl: GlobalTheory.KeyOriginEnlarge.etale_enlarge
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.EtaleEnlargeByUniformiserRoots
covers: 415
status: drafted
drafted_by: writer@claude
---
This theorem is the third of three enlargements in [the enlargement to a good model](/entry/enlarge-good/). It makes the integral closure of a $\mathbb{Z}/q$-torsor étale in codimension one over the base. The parent chain then gives the torsor a point. [Its statement form](/entry/etale-enlarge-by-uniformiser-roots/) repeats it.

## Statement

**Setting.** Let $T$ be a local domain in which each monic polynomial of positive degree has a root. Let $\mathfrak{o}_T = (\mathfrak{m}_T, X) \subset T[X]$. Let $T[X]_{\mathfrak{o}_T} \to O$ be a strict henselisation: $O$ is Henselian with separably closed residue field, and the map is local and ind-étale. Let $q > 0$ be a unit in $T$. For $R$ over a domain $A$, let $R_\eta$ be $R$ localized at $A \setminus 0$.

**Models.** A *model* over $A$ (`Fits`) is: a noetherian normal local domain $A$, essentially of finite type over $\mathbb{Z}$, with $q \in A^\times$ and an injective local $i \colon A \to T$; an étale $A[X]$-algebra $E$ with a prime $Q$ over $\mathfrak{o}_A$, and $R = E_Q$; maps $j \colon R \to O$ over $A[X] \to T[X]$ and $\psi \colon R_\eta \to O_\eta$ over $j$; and a $\mathbb{Z}/q$-torsor $D$ over $R_\eta$ (finite projective faithfully flat, and $D \otimes D \cong \prod_{\mathbb{Z}/q} D$).

A *retraction* (`Retracts`) is $\rho \colon R \to A$ with $\rho|_A = \mathrm{id}$, $\ker \rho = (X)$, and $i \circ \rho \equiv j \bmod XO$. Let $C$ be the integral closure of $R$ in $D$. A *point at zero* (`PointAtZero`) is a ring map $s \colon C \to \operatorname{Frac} A$ with $s|_R = \rho$. The model is *good* (`Good`) if it has a point at zero and $C_P$ is étale over $R_P$ for each prime $P$ of $R$ with $\operatorname{ht}(P \cap A) \leq 1$.

**Theorem.** Given a model over $A$ and a retraction $\rho$ with a point at zero, there is a model over some $A'$ with a good retraction $\rho'$, and ring maps $\beta \colon R_\eta \to R'_\eta$ and $h \colon D \to D'$ with $\psi' \circ \beta = \psi$ and $h$ compatible with $\beta$.

## Proof

1. `exists_ne_zero_closureEtaleAt_alt` gives $a \in A \setminus 0$ with $C_P$ étale over $R_P$ whenever $a \notin P$.
2. `exists_kummerEnlargement_rootsOfUniformisers` gives a larger ring $A \subseteq A_1$ of the same kind, with $i_1 \colon A_1 \to T$ that extends $i$, such that for each height one prime $\mathfrak{p}_1 \ni a$ of $A_1$, $\mathfrak{p} = \mathfrak{p}_1 \cap A$ has height one and a uniformiser of $A_{\mathfrak{p}}$ has a $q$-th root in $A_1$.
3. `baseChange_integralClosure_etale_height_one` carries the model, the retraction and the point at zero to $A_1$, and then $C_1$ is étale over $R_1$ at each prime of $R_1$ of height at most one.
4. `integralClosureEtaleAt_of_height_le_one_purity` extends this to each $P$ with $\operatorname{ht}(P \cap A_1) \leq 1$: its proof shows that $(R_1)_P$ is regular and applies a purity lemma.
5. `good_iff_etaleAt`, an `Iff.rfl`, adds the point at zero.

Steps 2 and 3 have the idea of Abhyankar's lemma (SGA 1, Exp. XIII, 5.2): adjoining $q$-th roots of uniformisers makes a tame cover of degree $q$ étale. Step 4 has the form of Zariski-Nagata purity (SGA 1, Exp. X, Thm. 3.1). We have not opened the proofs of steps 1 to 3.

## In the Lean code

It is in [EtaleEnlargeByUniformiserRoots.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EtaleEnlargeByUniformiserRoots.lean#L16). `Fits`, `Retracts` and `PointAtZero` are in [PointAtZero.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PointAtZero.lean#L12), `Good` in [ClosureFiniteEtale.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ClosureFiniteEtale.lean#L32). The four lemmas are second names of `exists_ne_zero_closureEtaleAt`, `KummerEnlarge.exists_kummer_enlargement`, `KeyOriginBC.etale_bc` and `closureEtaleAt_of_comap_height_le_one`.

The hypotheses on $O$ are only passed to step 3. The map $h$ need not respect the $\mathbb{Z}/q$-actions; the parent does not need this.
