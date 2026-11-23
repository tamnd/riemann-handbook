---
title: The crystalline step
decls:
  - UpperTheory.Gal.G3.vFin_holds
  - UpperTheory.Gal.Seam.matIn_holds
  - UpperTheory.Gal.Seam.crysStep_of
  - UpperTheory.Gal.Seam.crysStep_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The crystalline step

At a place $w \mid \ell$ where the tower has an onto good model, a Galois piece is crystalline. The proof embeds the piece into the cohomology of the generic fibre of the model and applies the crystalline comparison theorem of Faltings. A subrepresentation of a crystalline representation is crystalline, and so is a graded part. We first need the finiteness of $\ell$-adic cohomology.

**Theorem 3.3.1 (finiteness of $\ell$-adic cohomology).** Let $k$ be an algebraically closed field, $\ell$ a prime invertible in $k$, and $X$ a proper $k$-scheme. Then for all $n, i \in \mathbb{Z}$ the group $H^n(X, \mathbb{Z}_\ell(i))$ is a finitely generated $\mathbb{Z}_\ell$-module and $H^n(X, \mathbb{Q}_\ell(i))$ is a finite-dimensional $\mathbb{Q}_\ell$-space (SGA 4, XIV; J. S. Milne, *Étale Cohomology*, Chapter VI, §2).

Lean: `UpperTheory.Gal.G3.vFin_holds`.

*Proof.* For each $a \geq 1$ the groups $H^m(X, \mathbb{Z}/\ell^a(i))$ are finite; this is the [finiteness theorem](/entry/etale-finiteness-of-duality/) for proper schemes. The Bockstein sequences $0 \to \mathbb{Z}/\ell^b \to \mathbb{Z}/\ell^{a+b} \to \mathbb{Z}/\ell^a \to 0$ give long exact sequences in cohomology. With the finiteness at each level, they show that the inverse limit $H^n(X, \mathbb{Z}_\ell(i)) = \varprojlim_a H^n(X, \mathbb{Z}/\ell^a(i))$ is finitely generated: its reduction modulo $\ell$ injects into the finite group $H^n(X, \mathbb{Z}/\ell(i))$, and a complete module with finite reduction is finitely generated. Tensoring with $\mathbb{Q}_\ell$ gives the second claim. $\square$

Next we compare the piece with the cohomology of a model. Let $K$ be a finite extension of $\mathbb{Q}_\ell$ in $\overline{\mathbb{Q}}_\ell$, with ring of integers $\mathcal{O}_K$, and let $G_K = \operatorname{Gal}(\overline{\mathbb{Q}}_\ell/K)$. For an onto good model $C$ of a tower $(H, \theta)$ over $\mathcal{O}_K$, with smooth projective $Y \to \operatorname{Spec} \mathcal{O}_K$, write $V_n = H^n(Y_{\overline{\mathbb{Q}}_\ell}, \mathbb{Q}_\ell)$ for the cohomology of the geometric generic fibre, a representation of $G_K$.

**Proposition 3.3.2 (the piece embeds in the model).** Let $H$ be a nice Hecke tower over $K$, $\theta : \Gamma \to \overline{\mathbb{Q}}_\ell$, and $C$ an onto good model of $(H, \theta)$ over $\mathcal{O}_K$. Let $\rho_1 : G_K \to \mathrm{GL}_d(\overline{\mathbb{Q}}_\ell)$ be a matrix form of $\Pi_\theta$. Then there are $N \geq 0$, bases $b_n$ of $V_n$ for $n < N$, and a matrix $M$ with $d$ columns and an injective map $x \mapsto Mx$, such that for all $\sigma \in G_K$
$$\Bigl(\bigoplus_{n < N} \operatorname{mat}_{b_n}(\sigma)\Bigr)\, M = M\, \rho_1(\sigma).$$
Here $\operatorname{mat}_{b_n}(\sigma)$ is the matrix of $\sigma$ on $V_n$ in the basis $b_n$.

Lean: `UpperTheory.Gal.Seam.matIn_holds`.

*Proof.* The map $\pi : Z \to Y$ induces a pullback $\pi^* : H^*(Y_{\overline{\mathbb{Q}}_\ell}) \to H^*(Z_{\overline{\mathbb{Q}}_\ell})$. Since $Z \to Y_K$ is a finite étale Galois cover with group $\Delta$, $\pi^*$ is injective and its image is the $\Delta$-invariant part. Each $\delta \in \Delta$ acts as a Hecke operator with eigenvalue $1$, so $\Pi_\theta$ lies in the image of $\pi^*$. The map $\pi^*$ commutes with $G_K$ because $\pi$ is defined over $K$. The groups $V_n$ are finite-dimensional by the finiteness theorem, and they vanish for $n < 0$. The finitely many preimages below lie in finitely many degrees, so some $N$ bounds them. Choose bases $b_n$. The basis of $\Pi_\theta$ that defines $\rho_1$ has preimages under $\pi^*$, and $M$ is the matrix of their coordinates in the bases $b_n$. It is injective because $\pi^*$ is injective, and the equation holds because $\pi^*$ is Galois equivariant. $\square$

**Theorem 3.3.3 (crystalline comparison; Faltings).** Let $K \subset \overline{\mathbb{Q}}_\ell$ be a finite extension of $\mathbb{Q}_\ell$ and $Y$ a projective scheme over $\mathcal{O}_K$ that is strictly semistable for some uniformizer and smooth. Then for each $n$, the representation $H^n(Y_{\overline{\mathbb{Q}}_\ell}, \mathbb{Q}_\ell)$ of $G_K$ is [crystalline](/learn/galois-representations/#crystalline-de-rham-and-potentially-semistable-representations), that is, in every basis of $H^n$ the matrix of the Galois action is $B_{\mathrm{cris}}$-admissible (G. Faltings, Crystalline cohomology and $p$-adic Galois representations, in *Algebraic Analysis, Geometry, and Number Theory*, Johns Hopkins Univ. Press, 1989; T. Tsuji, $p$-adic étale cohomology and crystalline cohomology in the semi-stable reduction case, Invent. Math. 137 (1999)).

Lean: `CrystallineSemistableComparison.SmoothModelCrystalline` (the statement).

We take this theorem as given; it is an assumption of the next theorem.

**Theorem 3.3.4 (crystalline step).** Assume the crystalline comparison theorem (Theorem 3.3.3). Let $E$ be a number field, $\Omega$ an algebraic closure and $\ell$ a prime. Let $H$ be a nice Hecke tower over $E$, $\theta : \Gamma \to \overline{\mathbb{Q}}_\ell$, and $\rho$ a continuous Galois piece of $(H, \theta)$. Let $w$ be a place of $E$ above $\ell$ such that $(H, \theta)$ has an onto good model over $O_w$. Then for each place of $\Omega$ above $w$ and each identification of its decomposition group with $G_{E_w}$, the restriction of $\rho$ to the decomposition group is crystalline.

Lean: `UpperTheory.Gal.Seam.crysStep_of` (also `UpperTheory.Gal.Seam.crysStep_holds`, the same statement with the comparison theorem supplied).

*Proof.* Let $\rho$ be the graded part of a matrix form $\rho_0$. Fix a place of $\Omega$ above $w$ and its completion $E_w \subset \overline{\mathbb{Q}}_\ell$. The ring $O_w$ maps into $\mathcal{O}_{E_w}$, and a uniformizer maps to a uniformizer. Base change the tower and the good model along $E \to E_w$. The base changed tower is nice, the base changed model is again an onto good model, and the restriction of $\rho_0$ to the decomposition group is a matrix form $\rho_1$ of the piece of the base changed tower. By the Proposition, $\rho_1$ embeds into $\bigoplus_n V_n$ through the injective matrix $M$. Each $V_n$ is crystalline by Theorem 3.3.3, since $Y$ is projective and smooth over $\mathcal{O}_{E_w}$, and a smooth model is strictly semistable. A subrepresentation of a $B_{\mathrm{cris}}$-admissible representation is $B_{\mathrm{cris}}$-admissible, so $\rho_1$ is crystalline. The graded part of a crystalline representation along a stable flag is a sum of subquotients, so it is crystalline. Hence $\rho$ restricted to the decomposition group is crystalline. $\square$

**Remark 3.3.5 (Formalization).** Theorem 3.3.3 is `CrystallineSemistableComparison.SmoothModelCrystalline`, a hypothesis of `UpperTheory.Gal.Seam.crysStep_of`; `UpperTheory.Gal.Seam.crysStep_holds` supplies it as the first of three comparison statements in `UpperTheory.Gal.Seam.cstSmooth` (crystalline, de Rham, Frobenius). The proof of Proposition 3.3.2 uses `UpperTheory.Gal.Seam.hopEx_holds` (Hecke operators of a nice tower are correspondence operators), proved as `hopExS trivial` with the hypothesis `True` ([HopExS.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/HopExS.lean#L37)); `UpperTheory.Gal.G3.seamHopEx_holds` and `UpperTheory.Gal.G3.locTower_holds` in `TraceSplitHolds.lean` repeat it and `UpperTheory.Gal.Seam.locTower_holds`. The coefficient field is `Qbar l` in some places and `Om l` in others; we write $\overline{\mathbb{Q}}_\ell$ for both. A local datum at $w$ (`LocBridge`) is read here as the choice of a completion $E_w$ and of an identification of the decomposition group.
