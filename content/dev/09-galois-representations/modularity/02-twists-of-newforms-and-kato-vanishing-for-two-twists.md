---
title: Twists of newforms and Kato's vanishing for two twists
decls:
  - UpperTheory.V.Z.Kato.WeilSphericalRecords.TwistNewform.exists_newform_attached_twist_of_kills_mu
  - UpperTheory.V.Z.Kato.WeilSphericalRecords.twNew_alt
  - UpperTheory.V.Z.Kato.WeilSphericalRecords.twoS
  - UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH_of_rT_of_quadBC2
  - UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Twists of newforms and Kato's vanishing for two twists

This section proves that two Bloch-Kato Selmer groups vanish for a two-dimensional representation $W$ of $G_{\mathbb{Q}}$ that comes from a newform of odd weight and satisfies a list of conditions at an imaginary quadratic field. The two groups belong to $W$ and to its twist by the quadratic character of the field. The proof applies the [ordinary vanishing theorem](/entry/vanish-ord-l-of-zeta-ur/) twice. For the second application we need the twist of a newform by a character of finite order to be a newform again, and we prove this first. The result feeds the count I in [the window bound from the extended hypotheses](/entry/vwin-of-hypotheses-h-e-alt/). The background on [modular forms](/learn/automorphic-forms/#modular-forms), [Hecke characters](/learn/class-field-theory/#hecke-characters) and [local Bloch-Kato theory](/learn/padic-hodge/#local-bloch-kato-theory) is in Volume 1.

### Setting

Let $l$ be a prime, $\Omega$ an algebraic closure of $\mathbb{Q}$ and $G_{\mathbb{Q}} = \mathrm{Gal}(\Omega/\mathbb{Q})$. Fix a field isomorphism $\iota \colon \overline{\mathbb{Q}}_l \to \mathbb{C}$. Let $\varepsilon \colon G_{\mathbb{Q}} \to \overline{\mathbb{Q}}_l^\times$ be the [[cyclotomic character|XSGB5K2KEG]]. For a valuation ring $A$ of $\Omega$ let $D_A$ and $I_A$ be its decomposition and inertia groups, as in the chapter on [Hecke algebras](/entry/hecke-projector-newform-galois-image/). For a character $\varphi \colon G_{\mathbb{Q}} \to \overline{\mathbb{Q}}_l^\times$ and a representation $V \colon G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_l)$, the twist $\varphi \otimes V$ is $s \mapsto \varphi(s) V(s)$.

A character $\varphi$ *kills $\mu_N$* if $\varphi(s) = 1$ for each $s$ that fixes all $N$-th roots of unity. So $\varphi$ factors through $\mathrm{Gal}(\mathbb{Q}(\mu_N)/\mathbb{Q})$.

**Definition 8.2.1 (Attached newform).** Let $f$ be a newform of weight $k$ and level $M$. Then $f$ is *attached to $V$ via $\iota$* if $V$ is semisimple and, for all but finitely many primes $p$, the representation $V$ is trivial on $I_A$ for each $A$ over $p$, and for each Frobenius element $\sigma$ at $A$ the image under $\iota$ of the characteristic polynomial of $V(\sigma^{-1})$ is the Hecke polynomial of $f$ at $p$, given by the Satake parameters of $f$ at $p$.

### Twists of newforms

**Theorem 8.2.2 (Twists of newforms).** Assume the extended hypotheses of [Section 8.1.10](/entry/vwin-of-row/). Let $k \geq 2$, let $f$ be a newform of weight $k$ attached to $V$ via $\iota$, and let $\kappa$ be a character that kills $\mu_N$ for some $N \geq 1$. Then there is a newform $g$ of weight $k$ attached to $\kappa \otimes V$ via $\iota$.

Lean: `UpperTheory.V.Z.Kato.WeilSphericalRecords.TwistNewform.exists_newform_attached_twist_of_kills_mu`.

*Proof.* The rank $n$ package gives a global Artin map for $\mathbb{Q}$. The kernel of $\kappa$ contains the open subgroup that fixes $\mu_N$, so it is open and $\kappa$ has finite order $m$, the index of its kernel. By [global class field theory](/learn/class-field-theory/#global-class-field-theory) there is a unique Hecke character $\chi$ of finite order that corresponds to $\kappa$ through the Artin map. Since $\chi$ has finite order, its exponent at each archimedean place is $0$.

The newforms statement of the extended hypotheses gives a cuspidal automorphic representation $\pi$ of $\mathrm{GL}_2$ over $\mathbb{Q}$ with the infinitesimal character of weight $k$ and with Satake parameters $B_p$ at the primes $p$ that do not divide the level of $f$. The twist $\pi \otimes \chi$ is cuspidal, and its infinitesimal character is that of $\pi$, since the exponents of $\chi$ are $0$. So the same statement gives a newform $g$ of weight $k$ for $\pi \otimes \chi$.

The twist $\kappa \otimes V$ is semisimple, since $V$ is. Let $p$ be a prime that is not $l$, does not divide the levels of $f$ and $g$, at which $\chi$ is unramified and at which $f$ satisfies the condition of attachment. All but finitely many primes have these properties. Then $\kappa$ is trivial on $I_A$, so $\kappa \otimes V$ is trivial on $I_A$. For a Frobenius element $\sigma$ at $A$ we have $\iota\kappa(\sigma^{-1}) = \chi(p)$. The Satake parameters of $g$ at $p$ are $\chi(p) B_p$, by uniqueness of Satake parameters for the twist. So the characteristic polynomial of $\kappa(\sigma^{-1}) V(\sigma^{-1})$ is the Hecke polynomial of $g$ at $p$. $\square$

**Definition 8.2.3 (Admitted representation).** Let $e \geq 0$. A representation $W \colon G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_l)$ is *admitted for $(\iota, e)$* if:

1. $W$ is continuous and $(\det W)^2 = 1$;
2. $\det W(c) = -1$ for each complex conjugation $c$;
3. $W$ is irreducible on $H = \ker \varepsilon \cap \ker \det W$;
4. $W$ has a level $M \geq 1$ away from $l$;
5. there are a newform $f$ of weight $2e + 1$, an integer $M \geq 1$ and a character $\varphi$ that kills $\mu_M$ such that $f$ is attached to $\varepsilon^{-e}\varphi \otimes W$;
6. there are a valuation ring $A$ over $l$, a character $\chi$ that kills $\mu_l$ and a flag of $W$ on $D_A$ on which $I_A$ acts by $\varepsilon^{e}\chi$ on the line and by $\varepsilon^{-e}\chi$ on the quotient, and $I_A \subseteq \ker \det W$.

**Theorem 8.2.4 (Twists of admitted representations).** Assume the extended hypotheses. Let $l \neq 2$, $e \geq 1$, and let $W$ be admitted for $(\iota, e)$. Let $M \geq 1$ and let $\varphi$ kill $\mu_M$. Then there is a newform $g$ of weight $2e + 1$ attached to $\varepsilon^{-e} \otimes (\varphi \otimes W)$ via $\iota$.

Lean: `UpperTheory.V.Z.Kato.WeilSphericalRecords.twNew_alt`.

*Proof.* Condition 5 gives $f$, $M'$ and $\varphi'$ killing $\mu_{M'}$ with $f$ attached to $\varepsilon^{-e}\varphi' \otimes W$. The character $\varphi\varphi'^{-1}$ kills $\mu_{MM'}$, since an element that fixes $\mu_{MM'}$ fixes $\mu_M$ and $\mu_{M'}$. By Theorem (Twists of newforms) with $k = 2e + 1 \geq 2$, there is a newform $g$ of weight $2e+1$ attached to $\varphi\varphi'^{-1} \otimes (\varepsilon^{-e}\varphi' \otimes W)$. This twist is $\varepsilon^{-e} \otimes (\varphi \otimes W)$. $\square$

### Sources and the two vanishings

**Definition 8.2.5 (Spherical at $l$).** The representation $W$ is *spherical at $l$ for $(\iota, e)$* if the following holds for each $M \geq 1$ and each $\varphi$ that kills $\mu_M$. Let $A$ be a valuation ring over $l$ and let $\varphi \otimes W$ have a flag on $D_A$ on which $I_A$ acts by $\varepsilon^{e}$ and $\varepsilon^{-e}$. Then each regular algebraic cuspidal representation $\pi$ of $\mathrm{GL}_2$ over $\mathbb{Q}$ that is attached to $\varphi \otimes W$ via $\iota$ has Satake parameters at $l$.

**Definition 8.2.6 (Ordinary source).** The representation $W$ has an *ordinary source for $(\iota, e)$* if there are a newform $g$ of weight $2e + 1$ with $l$ prime to its level and $|\iota^{-1} a_l(g)| = 1$, a character $\chi$ that kills $\mu_l$, and a valuation ring $A$ over $l$ with a flag $(\kappa_0, \kappa_1)$ of $W$ on $D_A$, such that $g$ is attached to $\varepsilon^{-e}(\det W)^{-1}\chi \otimes W$ and $\kappa_1 \varepsilon^{e}(\det W)^{-1}\chi = 1$ on $I_A$; and if, for each $A$ over $l$ and each flag $(\kappa_0, \kappa_1)$ of $W$ on $D_A$, the character $\kappa_0$ is not $\varepsilon$ on $D_A$.

We use two results that are proved elsewhere. The first is the [ordinary vanishing theorem](/entry/vanish-ord-l-of-zeta-ur/), with the [unramified zeta theorem](/entry/zeta-ur/) of Section 3 as its input: assume the twelve statements on Galois cohomology of the rank $n$ package; if $l \neq 2$, $e \geq 1$ and $W$ is admitted for $(\iota, e)$ with an ordinary source, then the Bloch-Kato Selmer group of $W$ vanishes. The second is the *source statement*: if $l \neq 2$, $e \geq 1$ and $W$ is admitted for $(\iota, e)$ and spherical at $l$, then $W$ has an ordinary source.

**Definition 8.2.7 (Kato conditions).** Let $K$ be a number field, $e, N \geq 0$, and let $\theta, \psi$ be characters of $G_{\mathbb{Q}}$. The data $(l, K, e, N, \theta, \psi, W)$ satisfy the *Kato conditions* if:

1. $l \neq 2$, $e \geq 1$ and $l - 1$ does not divide $2e$;
2. $K$ is an imaginary quadratic field, $l$ does not divide $|d_K| h_K$, and $N \geq 1$ is even and prime to $d_K$;
3. $\theta$ is the quadratic character of $K$, so $\ker\theta = G_K$ and $\theta^2 = 1$;
4. $\psi$ kills $\mu_N$, its order is prime to $l$, and $\psi^2 = 1$ on $I_A$ for each $A$ over $l$;
5. $\varepsilon^{e}\psi(c) = 1$ for some complex conjugation $c$;
6. $W$ has level $N|d_K|$ with weights $(e, -e)$ and is ordinary with these weights;
7. $\det W = \theta$;
8. on $I_A$ for $A$ over $l$, the trace of $W$ is $\varepsilon^{e}\psi + (\varepsilon^{e}\psi)^{-1}$;
9. for all $g$, $\bigl|\operatorname{tr} W(g) - \theta(g)\,\varepsilon^{e}\psi(g) - (\varepsilon^{e}\psi)^{-1}(g)\bigr| < 1$;
10. there are $A$ over $l$, a character $\chi$ that kills $\mu_l$ and a flag of $W$ on $D_A$ with inertia characters $\varepsilon^{e}\chi$ and $\varepsilon^{-e}\chi$, and $I_A \subseteq \ker\theta$;
11. $W$ is irreducible on the subgroup of $G_K$ where the cyclotomic character of $K$ is trivial.

Under the Kato conditions, if a newform of weight $2e + 1$ is attached to $\varepsilon^{-e} \otimes W$, then $\det W = \theta$ and $W$ is admitted for $(\iota, e)$.

**Theorem 8.2.8 (Two vanishings from sources).** Assume the twelve statements on Galois cohomology and the source statement. Let $(l, K, e, N, \theta, \psi, W)$ satisfy the Kato conditions, let $f$ be a newform of weight $2e + 1$ attached to $\varepsilon^{-e} \otimes W$ via $\iota$, and let $W$ be spherical at $l$ for $(\iota, e)$. Then the Bloch-Kato Selmer groups of $W$ and of $\theta \otimes W$ vanish.

Lean: `UpperTheory.V.Z.Kato.WeilSphericalRecords.twoS`.

*Proof.* The Kato conditions give $\det W = \theta$ and that $W$ is admitted. The source statement gives an ordinary source for $W$, and the ordinary vanishing theorem gives the first vanishing.

For the second, the kernel of $\theta = \det W$ is open, since $W$ is continuous and $\theta^2 = 1$. The character $\theta$ is abelian, so by the Kronecker-Weber theorem there is $M \geq 1$ with $\theta$ killing $\mu_M$. The twist $\theta \otimes W$ is again admitted for $(\iota, e)$. It is spherical at $l$: for $M' \geq 1$ and $\varphi$ killing $\mu_{M'}$ we have $\varphi \otimes (\theta \otimes W) = \varphi\theta \otimes W$, and $\varphi\theta$ kills $\mu_{MM'}$, so the condition for $\theta \otimes W$ is the condition for $W$ with the character $\varphi\theta$. The source statement and the ordinary vanishing theorem give the second vanishing. $\square$

The *witness condition* for $W$ says that for each imaginary quadratic field $K'$ on which $W$ stays irreducible, the restriction of $W$ to $G_{K'}$ has an automorphy witness via $\iota$. We do not unfold the witness.

**Theorem 8.2.9 (Kato's vanishing for two twists).** Assume the extended hypotheses, the Galois row and quadratic base change for $\mathrm{GL}_2$. Let $(l, K, e, N, \theta, \psi, W)$ satisfy the Kato conditions, let $f$ be a newform of weight $2e + 1$ attached to $\varepsilon^{-e} \otimes W$ via $\iota$, and let $W$ satisfy the witness condition. Then the Bloch-Kato Selmer groups of $W$ and of $\theta \otimes W$ vanish.

Lean: `UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH_of_rT_of_quadBC2`.

*Proof.* The extended hypotheses, the row and quadratic base change give a local statement at $l$: local-global compatibility at $l$ for the representations attached to cuspidal representations of $\mathrm{GL}_2$, with spherical components and Frobenius roots. From it and Theorem (Twists of admitted representations), the extended hypotheses give the source statement. So Theorem (Two vanishings from sources) applies, and it remains to prove that $W$ is spherical at $l$.

The Kato conditions give that $W$ is admitted. So $W$ is continuous and irreducible on $H$, and then $W$ is irreducible, since an invariant line of $W$ is invariant under $H$. The extended hypotheses turn the witness condition and the local statement into sphericity at $l$, for continuous irreducible $W$ with $\det W$ killing some $\mu_M$. By the Kronecker-Weber theorem, as in the last proof, such an $M$ exists. $\square$

**Theorem 8.2.10 (Kato's vanishing from the extended hypotheses).** Assume the extended hypotheses. Under the Kato conditions, the newform condition and the witness condition, the Bloch-Kato Selmer groups of $W$ and of $\theta \otimes W$ vanish.

Lean: `UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH`.

*Proof.* The Galois row is one of the fifteen global statements of the rank $n$ package, and quadratic base change for $\mathrm{GL}_2$ is a theorem, proved in a later section. This is Theorem (Kato's vanishing for two twists) applied to the extended hypotheses, the row and quadratic base change. $\square$

**Remark 8.2.11 (Formalization).** In the proof of the vanishing for two twists, the equality $\det W = \theta$ is obtained and not used ([KatoTwoWOfPublishedH.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/KatoTwoWOfPublishedH.lean#L41)). The last theorem passes the row through `UpperTheory.Gal.SV.rowOf'`, which is the identity ([GaloisRepExistsTotallyRealGL2.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RankTwoPatching/GaloisRepExistsTotallyRealGL2.lean#L60)), and quadratic base change is the theorem `UpperTheory.ConvolutionTheory.R2.quadBC2`. The file sets `maxHeartbeats 800000` at line 29. The line `example : type_of% @KatoTwo := @KatoTwoW` ([KatoTwoW.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SphericalDecomposition/KatoTwoW.lean#L16)) only checks that the witness version is a proposition; it does not compare it with the version without the witness condition. The Kato conditions are the structure `Used` ([KatoTwoOfUseN.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/KatoTwoOfUseN.lean#L11)); its level and ordinarity conditions, the level away from $l$, the witness `WitA` and the source statement `SrcS` are not unfolded here. The twist lemma for sphericity is private ([SphAtTw.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SphericalDecomposition/SphAtTw.lean#L9)). The source statement comes from `srcS_alt`, the local statement from `locQ_of_alt` and the passage to sphericity from `sphOfWit`; we read them as statements.
