---
title: Eigenspace splitting on normal models
decls:
  - GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage5
  - GlobalTheory.T.model_over_mod_p_lattice_eigen_split
  - GlobalTheory.CompanionTheory.Ar.Num.GoodModel.relations
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Eigenspace splitting on normal models

This section proves the last link of the chain of refinements of the previous section: on a model whose chart rings are integrally closed, a lattice family with the two good properties and the line condition satisfies the Chern number relations. It is used in [stage 4](/entry/stage4/). The proof first shows that on such a model the lattice data have six exact properties on each chart, which we call the facts. From the facts the Chern numbers of the bundles of the family split into sums of Chern numbers of line bundles, one for each eigenspace of the characters $\chi_\tau$ modulo $p$. The relations then follow from two identities between these line bundles and a short computation.

We keep the notation of the previous section: $O$, $\varpi$, $\Omega$, the coordinates $x$ with charts $K$, the relative dimension $d$, the labels $Sg$ with ranks $r$, $s$, the finite set $F$, the prime $p$, the element $w$, the characters $\chi_\tau$ and the permutation $\varphi$.

### Lattice data on a chart

Let $R \subseteq \Omega$ be a chart ring. A lattice here is an additive subgroup of a finite dimensional vector space over $\Omega$. The standard lattice $\mathrm{std}$ of $\Omega^m$ is $R^m$. For $c \in \Omega$ and a lattice $L$ we write $cL$ for its image under multiplication by $c$ and $c^{-1}L$ for its preimage. For a lattice $L \subseteq \Omega^m$ the dual $L^\vee$ is the set of $v$ with $l \cdot v \in R$ for all $l \in L$.

**Definition 5.6.1 (Lattice data).** Let $n \in \mathbb{N}$. Lattice data on $R$ consist of a lattice $M$ in the space $\Omega^{F^n}$ of functions on $F^n$, and for each $\tau \in Sg$ lattices $\mathrm{lie}_\tau, W_\tau \subseteq \Omega^{r_\tau}$ and $\mathrm{om}_\tau, \mathrm{om}^{\mathrm{HT}}_\tau \subseteq \Omega^{s_\tau}$, and three correspondences
$$\Gamma_\tau \subseteq \Omega^{r_\tau} \times \Omega^{n}, \qquad \Delta_\tau \subseteq \Omega^{n} \times \Omega^{s_\tau}, \qquad \Theta_\tau \subseteq \Omega^{F^n} \times \Omega^{r_\tau}.$$

Lean: `GlobalTheory.CompanionTheory.Ar.Num.LieLatticeData`.

We use only the formal properties below. For a character $\chi : F \to \Omega$ let $\lambda_\chi : \Omega^n \to \Omega^{F^n}$ be the linear map that sends the basis vector $e_i$ to the function $a \mapsto \chi(a_i)$. Let $\mathrm{van}_i \subseteq \Omega^{F^n}$ be the functions that vanish at every $a$ with $a_j = 0$ for all $j \ge i$, and let $\mathrm{ann}_i \subseteq \Omega^n$ be the vectors whose coordinates of index less than $i$ are $0$.

**Definition 5.6.2 (Derived lattices).** For lattice data on $R$, a character $\chi$ and $i < n$:
- $l_1 = M + p\,\mathrm{std}$, and $\mathrm{af}_\chi = \lambda_\chi^{-1}(l_1)$;
- $h_\chi = \mathrm{af}_\chi^\vee$;
- $\mathrm{d}_{\chi, i}$ is the set of $i$-th coordinates of the vectors in $\mathrm{af}_\chi \cap \mathrm{ann}_i$;
- $\mathrm{x}_{\chi, i}$ is the set of $c \in \Omega$ with $c \, \chi(a_i) \in M + \mathrm{van}_{i+1}$, as functions of $a$;
- $\mathrm{im}_{\tau, \chi}$ is the projection to $\Omega^{s_\tau}$ of $\Delta_\tau \cap (h_\chi \times \Omega^{s_\tau})$, and $\ker_{\tau, \chi}$ is the projection to $\Omega^{r_\tau}$ of $\Gamma_\tau \cap (\Omega^{r_\tau} \times h_\chi)$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.LieLatticeData.af` (also `l1`, `hh`, `dId`, `xId`, `imH` and `kerH`).

The lattice $\mathrm{x}_{\chi, i}$ is the $i$-th distinguished lattice of the line condition. There are two more lattices: $k_{\tau, i}$, the projection to $\Omega^{r_\tau}$ of $\Theta_\tau \cap (\mathrm{van}_i \times \Omega^{r_\tau})$, and the step graph $S_{\tau, \chi, i} \subseteq \Omega \times \Omega^{r_\tau}$, the set of $(c, m)$ with $(c \, \chi(a_i), m) \in \Theta_\tau + (\mathrm{van}_{i+1} \times 0)$.

**Definition 5.6.3 (Good properties).** Call a lattice $L$ locally free of rank $m$ if it is a locally free $R$-module of rank $m$, and call a subspace $U$ a summand of $L$ if there is a linear projection onto $U$ that maps $L$ into $L$. The data satisfy $\mathrm{Good}_1$ if $l_1$ is locally free of rank $|F|^n$, the image of $\lambda_{\chi_\tau}$ is a summand of $l_1$ for each $\tau$, and $\mathrm{van}_i$ and $\mathrm{van}_{i+1} + \Omega \cdot \chi_\tau(a_i)$ are summands of $M$. They satisfy $\mathrm{Good}_2$ if each $\mathrm{ann}_i$ is a summand of $\mathrm{af}_{\chi_\tau}$, and $k_{\tau, i}$, the second projection of $S_{\tau, \chi_\tau, i}$ and $\mathrm{im}_{\tau, \chi_\tau}$ are locally free of ranks $r_\tau$, $r_\tau$ and $s_\tau$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.LieLatticeData.Good₁` (also `LieLatticeData.Good₂`).

**Definition 5.6.4 (Facts).** The lattice data on $R$ satisfy the facts for $p$, $w$, $\chi$ and $\varphi$ if for all $\tau$ and $i$:
1. $w \, \mathrm{std} \subseteq \mathrm{af}_{\chi_\tau}$;
2. $\mathrm{im}_{\tau, \chi_\tau} = \mathrm{om}_\tau$;
3. $\ker_{\tau, \chi_\tau} = w^{-1} \mathrm{lie}_\tau$;
4. $\mathrm{d}_{\chi_\tau, i} = \mathrm{x}_{\chi_\tau, i}$;
5. the second projection of $S_{\tau, \chi_\tau, i}$ is $k_{\tau, i}$;
6. the set of $c$ with $(c, 0) \in S_{\varphi\tau, \chi_{\varphi\tau}, i}$ is the $R$-span of the $p$-th powers of the elements of $\mathrm{x}_{\chi_\tau, i}$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.LieLatticeData.Facts`.

The first fact is the annihilator condition of the previous section. The sixth fact is the only one that relates the label $\varphi\tau$ to the label $\tau$, through $p$-th powers.

### The relations on a good model

**Theorem 5.6.5 (Relations on a model with the facts).** Let $x$ be a model of relative dimension $d$ over $O$, let $p$ be prime and let $D$ be a lattice family on $x$. Assume that on each chart the data of $D$ satisfy $\mathrm{Good}_1$, $\mathrm{Good}_2$ and the facts for $p$, $w$, $\chi$ and $\varphi$, and that $D$ satisfies the line condition. Then every choice of bundles $\mathrm{Lie}$, $W$, $\mathrm{Om}$ and $\mathrm{Om}^{\mathrm{HT}}$ that belong to $D$ satisfies the Chern number relations.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.GoodModel.relations` (also `GlobalTheory.T.model_over_mod_p_lattice_eigen_split`, a second name).

*Proof.* Since $x$ is a model, $O \to \Omega$ is injective. The element $w$ is not $0$, since $w^{p-1} = up$ with $u$ a unit and $p \ne 0$ in $O$. So $p = c w$ with $c = u^{-1} w^{p-2} \in O$, and the lattice data on each chart satisfy the character conditions: $p \neq 0$, $w \in R$, $p \in Rw$, $\chi_\tau(0) = 0$, $\chi_\tau(1) = 1$ and $\chi_\tau(F) \subseteq R$.

We build bundles from the derived lattices. By the gluing lemma for lattice families, for each $\tau$ and $i$ the lattices $\mathrm{x}_{\chi_\tau, i}$ on the charts glue to a line bundle $X_{\tau, i}$, and the lattices $h_{\chi_\tau}$ glue to a bundle $H_\tau$ of rank $n$. Let $T$ be the trivial line bundle, $T_n$ the trivial bundle of rank $n$, and $\mathrm{La}_\tau = w^{-1} \mathrm{Lie}_\tau$. By the base condition of $D$ we have $\mathrm{Lie}_\tau \subseteq W_\tau \subseteq \mathrm{La}_\tau$ and $\mathrm{Om}^{\mathrm{HT}}_\tau \subseteq \mathrm{Om}_\tau \subseteq w^{-1}\mathrm{Om}^{\mathrm{HT}}_\tau$, so $\mathrm{Om}_\tau$ and $\mathrm{Om}^{\mathrm{HT}}_\tau$ have the same generic fibre.

Fix $k$, $L$ and $Q$ as in the definition of the relations, and write $\operatorname{ck}(E, E')$ for $c_k(E, E'; L, Q)$. Three results of the development give the identities that we need. All three use $\mathrm{Good}_1$ and the facts; the first and the third also use $\mathrm{Good}_2$ and the line condition. The first is the eigenspace splitting: $H_\tau$ and $T_n$ have the same generic fibre and
$$\operatorname{ck}(H_\tau, T_n) = (-1)^k \sum_{i < n} \operatorname{ck}(X_{\tau, i}, T).$$
The second is an exact sequence of quotients: the quotients $\mathrm{La}_\tau / W_\tau$, $H_\tau / T_n$ and $\mathrm{Om}_\tau / \mathrm{Om}^{\mathrm{HT}}_\tau$ form an exact sequence on each chart. A Hodge-Tate intersection identity for such a sequence then gives
$$\operatorname{ck}(\mathrm{Lie}_\tau, W_\tau) + \operatorname{ck}(\mathrm{Om}_\tau, \mathrm{Om}^{\mathrm{HT}}_\tau) = \operatorname{ck}(H_\tau, T_n) - k\, \nu_\tau(w),$$
where $\nu_\tau(w)$ is the root number of $\mathrm{Lie}_\tau$ for the power sum of degree $k - 1$ at $w$. The third is the Frobenius identity:
$$k \, \nu_{\varphi\tau} = (-1)^{k-1} \sum_{i < n} \bigl( \operatorname{ck}(X_{\varphi\tau, i}, T) - p^k \operatorname{ck}(X_{\tau, i}, T) \bigr),$$
with $\nu_{\varphi\tau}$ the root number at $p$. Last, the root number is additive in the element: since $w^{p-1} = up$ with $u$ a unit, $(p - 1)\, \nu_\tau(w) = \nu_\tau$.

Put $h(\tau) = (-1)^k \sum_i \operatorname{ck}(X_{\tau, i}, T)$. The first two identities give $c_\tau = h(\tau) - k \nu_\tau(w) = h(\tau) - k \nu_\tau / (p - 1)$, where we divide by $p - 1 \ge 1$ in $\mathbb{R}$. Multiply the Frobenius identity by $(-1)^k$ and use $(-1)^{k-1}(-1)^k = -1$: then $k \nu_{\varphi\tau} = p^k h(\tau) - h(\varphi\tau)$. These are the two relations. $\square$

### Normal charts

**Theorem 5.6.6 (Stage 5).** Let $x$ be a model of relative dimension $d$ over $O$ with function field $\Omega$, let $p$ be prime, and let $D$ be a lattice family on $x$. Assume that the chart rings of $x$ are integrally closed in $\Omega$, that on each chart the data of $D$ satisfy $\mathrm{Good}_1$ and $\mathrm{Good}_2$, and that $D$ satisfies the line condition. Then every choice of bundles that belong to $D$ satisfies the Chern number relations.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage5`.

*Proof.* We show that the data of $D$ satisfy the facts on each chart; then the theorem on relations on a model with the facts gives the claim. Fix a chart with ring $R$. The data satisfy the character conditions, as in the proof above, and the base condition of a lattice family. The ring $R$ is noetherian. Since the function field of $x$ is $\Omega$, the fraction field of $R$ is $\Omega$. By assumption $R$ is integrally closed. The test condition of a lattice family says that the facts hold after base change to every test point: a ring $R_C$ in an algebraically closed field $C$ over $\Omega$ that is the ring of a valuation $v$ with $v(p) < 1$, is $p$-adically complete, and contains the image of $R$. A lemma of the development on normal rings then says that the facts hold on $R$ itself, given $\mathrm{Good}_1$ and $\mathrm{Good}_2$. $\square$

**Remark 5.6.7 (Formalization).** Stage 5 has no hypothesis that $O$ has characteristic $0$, while [stage 4](/entry/stage4/) has one ([DescentRelationsFromModels.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/DescentRelationsFromModels.lean#L99)). The theorem on relations on a model with the facts asks for neither normality nor the function field. The second name only calls the first with `first | exact @…`. The lemma that gives the facts on normal rings, the gluing lemma, and the three identities in the proof are results of the development that this chapter does not cover. We do not unfold the test condition or the compatibility of the data between the charts.
