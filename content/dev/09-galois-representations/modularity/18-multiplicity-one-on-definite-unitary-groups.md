---
title: Multiplicity one on definite unitary groups
decls:
  - UpperTheory.V.Z.Mult.stableBlockSA
  - UpperTheory.V.Z.Mult.mult_free
  - UpperTheory.V.Z.Desc.V0.flathE
  - UpperTheory.V.Z.Desc.V0.countE'_alt
  - UpperTheory.V.Z.Desc.V0.numJEDenseThresholdCases
  - UpperTheory.V.Z.J.D.numJ'_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Multiplicity one on definite unitary groups

This section proves a multiplicity one statement for automorphic forms on definite unitary groups in rank at most four, and uses it to compare the multiplicities of two points of the same weight in a Hida family. Section 19 uses the comparison to prove that three-dimensional Hida families are modular, and through it the counts I and V of section 1 depend on it. The multiplicity statement comes from the stable trace formula. The comparison comes from a tensor product factorization of automorphic forms and from the count of descents.

Throughout, $E$ is a CM field with maximal totally real subfield $E^{+}$, and $U$ is a definite unitary group in $n$ variables attached to $E/E^{+}$. We assume that $E$ satisfies the unramified condition for base change from $U$ to $\mathrm{GL}_n$ (we do not unfold this condition). A place $w$ of $E$ is split if it lies over a place of $E^{+}$ that splits in $E$; at a split place, $U(E^{+}_w) \cong \mathrm{GL}_n(E_w)$. For a dominant weight $\lambda$ at the infinite places, let $\mathcal{A}(\lambda, K')$ be the space of automorphic forms on $U$ of weight $\lambda$ that are fixed by an open compact subgroup $K' = \prod_w K'_w$.

**Definition 8.18.1 (Decomposition, matching).** Let $S$ be a set of places and $K'$ a level with $K'_w$ hyperspecial at each place that is not split. A decomposition of $\mathcal{A}(\lambda, K')$ is a finite family $(\sigma_i)$ of automorphic representations of $U$ of weight $\lambda$ such that each $\sigma_i^{K'} \ne 0$, the spaces $\sigma_i^{K'}$ are independent, and their sum is $\mathcal{A}(\lambda, K')$. Let $\pi$ be a cuspidal representation of $\mathrm{GL}_n(\mathbb{A}_E)$. We say that $\sigma$ matches $\pi$ if, at all but finitely many split places $w$, the representation $\sigma_w$ has a constituent $\tau$ with the same Satake parameter as $\pi_w$.

A representation that matches $\pi$ is a weak descent of $\pi$ to $U$. The multiplicity statement says that the number of such descents in a decomposition depends only on the weight.

**Theorem 8.18.2 (Isolation in the stable trace formula).** Let $1 \le n$ and let $\lambda$ be a dominant weight. There is $c_0 > 0$ with this property. Let $\pi$ be a regular algebraic cuspidal representation of $\mathrm{GL}_n(\mathbb{A}_E)$ whose dual is its complex conjugate, with infinity type given by $\lambda$. Let $Z$ be a finite set of split places, $B_w$ the Satake parameter of $\pi_w$ for $w \notin Z$, and $\tau_w$ a component of $\pi$ at $w \in Z$. Then there is $c \in \mathbb{C}$ with $|c| = c_0$ such that, for each test function $\varphi = \otimes_{w \in Z} \varphi_w$ that is bi-invariant under the standard maximal compact subgroups and regular at some $w \in Z$, there are finitely many conjugate self-dual data $D_j$, with Satake parameters $B_{1,j}$, none of which contains $\pi$, with the infinity type of $\lambda$, with this property: for each finite set $T$ of split places disjoint from $Z$ and each $\rho > 0$ larger than the absolute values of the Hecke eigenvalues of the $D_j$ at $T$, the stable geometric side of the trace formula for the $k$-th power of the Hecke operator at $T$ differs from

$$c \prod_{w \in Z} \operatorname{tr} \tau_w(\varphi_w) \cdot \lambda_T(B)^{k}$$

by a term that is small with respect to $\rho^{k}$ as $k \to \infty$.

Lean: `UpperTheory.V.Z.Mult.stableBlockSA`.

*Proof.* The stable trace formula for $U$ is compared with the twisted trace formula for $\mathrm{GL}_n$ over $E$. On the spectral side, the representations with Hecke eigenvalue $\lambda_T(B)$ at $T$ contribute the main term, and the constant $c$ comes from the stable multiplicity of $\pi$; the other cuspidal data contribute terms of exponential size at most $\rho^{k}$. The comparison uses the finiteness of the cuspidal spectrum of fixed level and weight, the admissibility of the spectral terms, a growth bound for the terms of the twisted trace, the separation of unitary characters by their Hecke eigenvalues, and the fact that the spectral expansion converges absolutely. $\square$

**Theorem 8.18.3 (Multiplicity of descents).** Let $1 \le n \le 4$ and let $\lambda$ be a dominant weight. Then there is an integer $a > 0$ with this property. Let $\pi$ be a regular algebraic cuspidal representation of $\mathrm{GL}_n(\mathbb{A}_E)$ whose dual is its complex conjugate, with infinity type given by $\lambda$ and unramified at each place that is not split. Let $S$ be a section of the places and $K'$ a level that is hyperspecial at the places that are not split, such that at each split $w \in S$ the representation $\pi_w$ has a component with nonzero $K'_w$-fixed vectors. Then for each decomposition $(\sigma_i)$ of $\mathcal{A}(\lambda, K')$, exactly $a$ of the $\sigma_i$ match $\pi$.

Lean: `UpperTheory.V.Z.Mult.mult_free`.

*Proof.* The local statement at split places comes first: a representation $\sigma$ that matches $\pi$ and is unramified at the places that are not split has, at every split place $w$, the component of $\pi_w$ as a constituent of $\sigma_w$. This follows from strong multiplicity one for $\mathrm{GL}_n$, the classification of Jacquet and Shalika, and the uniqueness of the matching of local components. Then we count. The trace of a Hecke operator on $\mathcal{A}(\lambda, K')$ is a sum over the $\sigma_i$. The [Theorem 8.18.2](/entry/stable-block-sa/) on isolation shows that, after a high power of a Hecke operator at a set $T$ that separates $\pi$ from the other data, only the $\sigma_i$ that match $\pi$ survive, and each contributes the same local trace at the places of $Z$. Comparing the two sides gives the number of $i$ with $\sigma_i$ matching $\pi$ as $c_0$ divided by the contribution of one $\sigma_i$; this number $a$ is a positive integer that depends only on $\lambda$. $\square$

We come to Hida families. We keep the Hida setting $s$ over a CM field $L$ of section 10, with level $V$, a residual representation $r$ of rank $n$ with $1 \le n \le 4$, the universal ordinary determinant ring $B$ of $r$, a weight algebra $\Lambda$ and $\iota \colon \overline{\mathbb{Q}}_l \cong \mathbb{C}$. Unitary Hecke data for $r$ consist of a definite unitary group over $L$, a weight, a type $\tau_0$ and a Hecke algebra $\mathbb{T}_K$ acting on ordinary forms of level $K$.

**Definition 8.18.4 (Ideal of Hecke type).** An ideal $J$ of $B$ is of Hecke type for the unitary Hecke data if either the space of ordinary forms of level $K$ is zero and $J = B$, or $J$ is the kernel of a surjection $f \colon B \to \mathbb{T}_K$ that sends the trace of each Frobenius element to the corresponding Hecke operator and is compatible with the weight maps from $\Lambda$.

**Definition 8.18.5 (Multiplicity comparison).** Let $J$ be an ideal of $B$. The multiplicity comparison holds for $(B, \Lambda, J)$ if there are a module $M$ over $B$ and $\Lambda$ and an idempotent $\Lambda$-endomorphism $\varepsilon$ of $M$ with this property: for points $x$ and $y$ of $B$ that vanish on $J$ and have the same weight, with $x$ arithmetic, $y$ good, and both irreducible, the multiplicities satisfy

$$1 \le \mu_{\varepsilon}(x) \le \mu_{\varepsilon}(y).$$

Here $\mu_\varepsilon(x)$ is the dimension of the $x$-part of $\varepsilon M$.

The next theorem is the tool for the comparison. It is a form of the tensor product theorem of Flath.

**Theorem 8.18.6 (Factorization of forms).** Let $\sigma$ be an automorphic representation of the unitary group of the Hida setting of weight $\lambda$, with nonzero space $V_\sigma$ of vectors of the given type and level. Let $C$ be a set of local components of $\sigma$, smooth representations $C_{\mathrm{L}}$ at the places above $l$ and $C_{\mathrm{S}}$ at the other places of $S$. Let $e$ be a basis of the algebraic representation of weight $\lambda$. Then there is an injective linear map

$$f \colon C_{\mathrm{L}} \boxtimes C_{\mathrm{S}} \longrightarrow \mathcal{A}, \qquad f(C_{\mathrm{L}} \boxtimes C_{\mathrm{S}}) = V_\sigma,$$

that intertwines the action of the group at the places of $S$.

Lean: `UpperTheory.V.Z.Desc.V0.flathE`.

*Proof.* Each $\sigma_w$ is irreducible, and the external tensor product of irreducible smooth representations is irreducible. The space $V_\sigma$ is the isotypic part of $\mathcal{A}$ for $\sigma$ at the places of $S$. By the irreducibility of the box product and by Schur's lemma for $\mathrm{GL}_n$, the isotypic part is a sum of copies of $C_{\mathrm{L}} \boxtimes C_{\mathrm{S}}$; the multiplicity is one because $V_\sigma$ is the image of the space of $\sigma$, and $\sigma$ is a restricted tensor product of its components. The infinite dimension of the components excludes the case of a finite-dimensional character. The weight basis $e$ fixes the identification at the infinite places. $\square$

**Theorem 8.18.7 (Dimensions of eigenparts).** Assume the extended hypotheses. Let $\lambda$ be a weight. Then there is $a_0$ with this property. Take a type $\tau_0$, a weight and a point $x$ of the Hida setting, a level $K$ and Hecke eigenvalues of absolute value one, such that the space of forms with these data is not zero and each automorphic representation that meets it is irreducible at $S$. Then there are a cuspidal representation $\pi$ of $\mathrm{GL}_n(\mathbb{A}_L)$, an automorphic representation $\sigma$ of the unitary group and local components $C$ of $\pi$ such that, for each Hecke element $a$, the dimension of the $a$-part of the space of forms is $a_0$ times the rank of the $a$-part of the invariants of $C$.

Lean: `UpperTheory.V.Z.Desc.V0.countE'_alt`.

*Proof.* Decompose the space of forms as a sum over automorphic representations $\sigma$. The representations that meet the space all match one $\pi$, by sphericity at the same places and the base change of the extended hypotheses. By the [Theorem 8.18.3](/entry/mult-free/) on multiplicity, exactly $a_0$ of them match $\pi$. By the [Theorem 8.18.6](/entry/flath-e/) on factorization, each contributes the invariants of $C_{\mathrm{L}} \boxtimes C_{\mathrm{S}}$, and the components at $S$ are those of $\pi$ by the local statement in the proof of the multiplicity theorem. The ordinary part has slope zero and multiplicity one at $l$, which identifies the $a$-parts. $\square$

**Theorem 8.18.8 (Multiplicity comparison in Hida families).** Assume the extended hypotheses, the multiplicity of descents and the local matching at split places. Let $1 \le n \le 4$, let $\Lambda$ be a domain, and let $J$ be a radical ideal of Hecke type. Then the multiplicity comparison holds for $(B, \Lambda, J)$.

Lean: `UpperTheory.V.Z.Desc.V0.numJEDenseThresholdCases` (also `UpperTheory.V.Z.J.D.numJ'_alt`, the same statement with the condition at $v_0$ on $r$).

*Proof.* If $J = B$ there are no points, and the zero module works. Otherwise let $M$ be the module of ordinary forms of the Hecke data. The [Theorem 8.18.7](/entry/count-e-prime-alt/) on eigenparts, with the Kirillov model at a place $v_0$ and the local inverse of the Hecke action there, gives a finitely supported function $a$ on $\mathrm{GL}_n(L_{v_0})$ and an integer $N$ prime to $l$ such that any two dimensions of the parts cut out by $(a, N)$ are equal and at least one. Let $\varepsilon$ be the idempotent attached to $(a, N)$. For points $x$ and $y$ as in the definition, $\mu_\varepsilon(x)$ and $\mu_\varepsilon(y)$ are two such dimensions. So $1 \le \mu_\varepsilon(x) = \mu_\varepsilon(y)$. $\square$

**Remark 8.18.9 (Formalization).** The isolation statement is the definition `StableBlockSA` ([StableBlockGA.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/MultiplicityOne/StableBlockGA.lean#L47)); we have not unfolded `Small`, `geomSt2`, `fam` or `val`, and our description of the smallness and of the stable geometric side reads these names. The multiplicity comparison is proved with equality in [TNumJE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TNumJE.lean#L171), but the statement keeps only $\le$; the second name drops the unused condition at $v_0$ ([ModNOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ModNOf.lean#L15)). The dimension theorem is one application of `count_e_of_sph_same_at_same_bc_dims`, which discards its inputs `ZEq` and `CompsEx` ([TCountE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TCountE.lean#L147)). The name `numJEDenseThresholdCases` does not describe a multiplicity comparison. The factorization theorem and its steps are summarized from the names of the lemmas it combines (`isotS`, `boxIrr`, `piIsot`, `schurGL`, `infDim`); we have not unfolded them.
