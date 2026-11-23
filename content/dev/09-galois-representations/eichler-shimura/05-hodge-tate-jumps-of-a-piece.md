---
title: Hodge-Tate jumps of a piece
decls:
  - UpperTheory.Gal.G3.hodgeBC_holds
  - UpperTheory.Gal.G3.jumpStep_of
  - UpperTheory.Gal.Int.Geo.jumpStep_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hodge-Tate jumps of a piece

The Hodge-Tate jumps of a Galois piece are read off from Hodge cohomology. If the Hecke eigensystem $\theta$ occurs in $H^b(Z, \Omega^a)$ over $\mathbb{C}$, then $a$ is a Hodge-Tate jump of the piece at each place above $\ell$ where the tower has a good model. The proof moves the eigenvector from $\mathbb{C}$ to the $\ell$-adic field, descends it to the model, and then applies the Hodge-Tate frames of [the previous section](/entry/ht-spec-good/).

**Definition 3.5.1 (Hodge cohomology and Hecke action).** Let $s : X \to \operatorname{Spec} k$ be a scheme over a field. Its *Hodge cohomology* is $H^b(X, \Omega^a_{X/k})$, a $k$-vector space. A map $f : X' \to X$ over $k$ induces a pullback $f^*$. A finite étale map $f$ induces a trace $f_*$. For a Hecke tower $H$ over $k$ with $s_g$ finite étale, the *Hecke operator* on Hodge cohomology is $s_{g*} t_g^*$. Let $\theta : \Gamma \to k$. A class $x \neq 0$ is a *Hodge $\theta$-eigenvector* if $s_{g*} t_g^* x = \theta(g)\, x$ for all $g$. The eigensystem $\theta$ *occurs in Hodge degree $a$* if some $H^b(Z, \Omega^a)$ contains a Hodge $\theta$-eigenvector.

Lean: `UpperTheory.Gal.Int.Geo.IsHEig`, `UpperTheory.Gal.Int.Geo.HOcc` (also `UpperTheory.Gal.Int.Geo.HodgeAt`).

For a tower $H$ over a number field $E$, an embedding $\tau : E \to \mathbb{C}$, an isomorphism $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$ and $\theta : \Gamma \to \overline{\mathbb{Q}}_\ell$, we say that $j \in \mathbb{Z}$ is a *Hodge jump of $(H, \theta)$ at $\tau$* if $j \geq 0$ and $\iota \circ \theta$ occurs in Hodge degree $j$ for the base change $H_\tau$ over $\mathbb{C}$.

**Theorem 3.5.2 (base change of Hodge cohomology).** Let $\varphi : k \to k'$ be a map of fields. For each cartesian square formed by $X' \to X$, $X \to \operatorname{Spec} k$, $X' \to \operatorname{Spec} k'$ and $\operatorname{Spec} \varphi$ there are $\varphi$-semilinear maps $\beta : H^b(X, \Omega^a_{X/k}) \to H^b(X', \Omega^a_{X'/k'})$ for all $a, b$, such that:

1. if $X$ is proper over $k$, then $\beta$ carries every $k$-basis to a $k'$-basis;
2. $\beta$ commutes with pullbacks along maps of such squares;
3. $\beta$ commutes with traces along maps of such squares that are finite étale on both levels.

In particular $k' \otimes_k H^b(X, \Omega^a_{X/k}) \cong H^b(X', \Omega^a_{X'/k'})$ for proper $X$ (flat base change; R. Hartshorne, *Algebraic Geometry*, Chapter III, Proposition 9.3).

Lean: `UpperTheory.Gal.G3.hodgeBC_holds`.

*Proof.* Hodge cohomology is computed by a Čech complex for an affine cover. Since $\Omega^a$ commutes with base change and $k'$ is flat over $k$, the Čech complex of $X'$ is the base change of the Čech complex of $X$. This gives $\beta$ and the base change of bases. Pullbacks commute with $\beta$ by naturality of the Čech construction. For a finite étale map the trace is defined locally by the trace of a finite free algebra, and this trace commutes with base change. $\square$

**Theorem 3.5.3 (Hodge-Tate jumps of a piece).** Let $E$ be a number field, $\Omega$ an algebraic closure, $\ell$ a prime and $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$. Let $H$ be a nice Hecke tower over $E$, $\theta : \Gamma \to \overline{\mathbb{Q}}_\ell$, and $\rho$ a continuous Galois piece of $(H, \theta)$. Let $w$ be a place of $E$ above $\ell$ such that $(H, \theta)$ has an onto good model $C$ over $O_w$ and, for each $g \in \Gamma$, a correspondence $(s, t)$ on the model over $O_w$, with $s$ finite étale of some degree, that lies under $g$. Then for each place of $\Omega$ above $w$, each identification of its decomposition group, and each embedding $\tau : E \to \overline{\mathbb{Q}}_\ell$ that induces the place, every Hodge jump of $(H, \theta)$ at $\iota \circ \tau$ is a [Hodge-Tate jump](/learn/galois-representations/#crystalline-de-rham-and-potentially-semistable-representations) of the restriction of $\rho$ at $\tau$.

Lean: `UpperTheory.Gal.Int.Geo.jumpStep_holds` (also `UpperTheory.Gal.G3.jumpStep_of`, the same statement with Theorems 1.4.7, 1.3.4 and 1.1.6 as hypotheses).

*Proof.* Let $j$ be a Hodge jump at $\iota \circ \tau$, with a Hodge $\iota\theta$-eigenvector $x \in H^b(Z_{\iota\tau}, \Omega^j)$.

First, move $x$ to $\ell$-adic coefficients. Let $E_w \subset \overline{\mathbb{Q}}_\ell$ be the completion at the place. By the base change theorem, Hodge cohomology of $Z$ over $E_w$, over $\overline{\mathbb{Q}}_\ell$ and over $\mathbb{C}$ (through $\iota$) are base changes of each other, with bases going to bases. The Hecke operators commute with these maps, because they are built from pullbacks and traces. So the eigensystem $\theta$ occurs in Hodge degree $j$ for the base change of $H$ to $E_w$.

Second, descend to the model. Over $E_w$ the onto good model gives a Galois cover $Z \to Y_{E_w}$ with group $\Delta$. Each element of $\Delta$ acts as a Hecke operator with eigenvalue $1$, and over a Galois cover the pullback of a trace is the sum over the sheets. So the eigenvector is $\Delta$-invariant and comes from the Hodge cohomology of $Y_{E_w}$. The correspondences on $Y$ that lie under each $g$ act on it by the eigenvalues $\theta(g)$, up to the degrees $m_g$.

Third, apply the Hodge-Tate frames. The model $Y$ is projective and smooth, so it is a smooth model in the sense of [the previous section](/entry/ht-spec-good/). By the frames theorem, $\mathbb{C}_\ell \otimes V_n \cong \bigoplus_a \mathbb{C}_\ell(-a) \otimes \mathrm{Hdg}^{a,n}$, and the isomorphism is natural for the correspondences on $Y$. So the $\theta$-eigenspace in $\mathrm{Hdg}^{j,n}$ matches a $\mathbb{C}_\ell(-j)$-part of the $\theta$-part of $\mathbb{C}_\ell \otimes V_n$. By the embedding of the piece in the model from [the crystalline step](/entry/mat-in-holds/), this $\theta$-part is the restriction of the piece to the decomposition group. Hence $j$ is a Hodge-Tate jump of the restriction of a matrix form $\rho_0$, at the embedding $\tau$. A graded part has the same Hodge-Tate jumps as $\rho_0$, so $j$ is a jump of $\rho$. $\square$

**Remark 3.5.4.** The theorem says only that each Hodge jump lies in the multiset of Hodge-Tate jumps of $\rho$. It does not compare multiplicities, and it does not say that every Hodge-Tate jump of $\rho$ is a Hodge jump. In $H^b(Z, \Omega^a)$ the index $a$ is the form degree, and the cohomological degree $b$ is free.

**Remark 3.5.5 (Formalization).** The conclusion of Theorem 3.5.3 is `JOcc`. `UpperTheory.Gal.Int.Geo.jumpStep_holds` is `UpperTheory.Gal.G3.jumpStep_of` applied to `UpperTheory.Gal.Seam.HT.htSpecGood`, `UpperTheory.Gal.Seam.crysStep_holds` and `UpperTheory.Gal.Int.Geo.repEx_holds`. The crystalline step is used only because Hodge-Tate jumps (`IsJumpsAt`) are defined for crystalline restrictions, and the existence of the jump multiset (`PositivityTheory.AutomorphicGaloisHodgeTate.G8.JumpsEx`) assumes it. `UpperTheory.Gal.G3.hodgeBC_holds` is built from the Čech base change theorem `PositivityTheory.AutomorphicGaloisHodgeTate.G8.HBC.cech_holds`.
