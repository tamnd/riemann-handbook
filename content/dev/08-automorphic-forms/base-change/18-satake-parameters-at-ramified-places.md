---
title: Satake parameters at ramified places
decls:
  - UpperTheory.ConvolutionTheory.Sph.ramSph
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Satake parameters at ramified places

A weak base change of a cuspidal representation is defined by the Satake parameters at almost all places. This section shows that the lift also keeps the Satake parameters at a place where the extension ramifies, provided that the representation below is unramified there. The result is a local statement: it combines the local base change of principal series from [the theorem on principal series](/entry/lift-good/) with the [Jacquet-Shalika bound](/entry/jacquet-shalika-bound/), which excludes the reducible unramified principal series. The construction of quadratic lifts uses it, below the step [EveryCharacter](/step/every-character/).

Throughout, $K$ and $M$ are totally complex number fields, $M/K$ is Galois of prime degree $\ell$, and $n \ge 1$. For a finite place $v$ of a number field let $N(v)$ be the order of its residue field. A cuspidal representation $\pi$ of $\mathrm{GL}_n$ over $K$ has [Satake parameters](/learn/representations/#unramified-representations) $B$ at $v$, a multiset of $n$ nonzero complex numbers, if $\pi_v$ is unramified with these parameters.

**Definition 7.18.1 (Weak base change).** Let $\pi$ and $\Pi$ be cuspidal representations of $\mathrm{GL}_n$ over $K$ and $M$. We say that $\Pi$ is a weak base change of $\pi$ if for all but finitely many finite places $w$ of $M$, with $v$ the place of $K$ below $w$, the following holds: for every $f \in \mathbb{N}$ with $N(w) = N(v)^f$ there is a Satake parameter $B$ of $\pi$ at $v$ such that $B^f = \{b^f : b \in B\}$ is a Satake parameter of $\Pi$ at $w$.

The exponent $f$ is the residue degree of $w$ over $v$, and the condition is the usual relation between Satake parameters and Frobenius under base change.

**Theorem 7.18.2 (Base change keeps Satake parameters at ramified places).** Let $\Pi$ be a weak base change of $\pi$. Let $w$ be a finite place of $M$ that is ramified over $K$, and let $v$ be the place below $w$. If $B$ is a Satake parameter of $\pi$ at $v$, then $B$ is a Satake parameter of $\Pi$ at $w$.

Lean: `UpperTheory.ConvolutionTheory.Sph.ramSph`.

We use the following facts.

1. (Ramified places.) Since $\ell$ is prime and $w$ is ramified, $w$ is the only place above $v$ and $w$ is totally ramified. So $N(w) = N(v)$, and $v$ does not split in $M$.
2. (Local Galois data.) Let $\sigma$ generate $\mathrm{Gal}(M/K)$. Since $v$ does not split, there are a generator $\sigma_w$ of the local Galois action on $M_w$ and the norm map $\mathrm{N} \colon M_w^\times \to K_v^\times$.
3. (Galois invariance and local components.) A weak base change $\Pi$ satisfies $\Pi \circ g \cong \Pi$ for $g \in \mathrm{Gal}(M/K)$, and $\pi$ and $\Pi$ have irreducible local components $\pi_v$ and $\Pi_w$.
4. (Base change of principal series.) If $\pi_v$ is a subquotient of the principal series $I(\omega_1, \dots, \omega_n)$ of smooth characters $\omega_i$ of $K_v^\times$, then $\Pi_w$ is a subquotient of $I(\omega_1 \circ \mathrm{N}, \dots, \omega_n \circ \mathrm{N})$. This is [the theorem on principal series](/entry/lift-good/).
5. (Satake parameters and principal series.) For $\alpha \in \mathbb{C}^\times$ let $\chi_\alpha$ be the unramified character of $K_v^\times$ with $\chi_\alpha(\varpi_v) = \alpha$. If $\pi$ has a Satake parameter at $v$, then $\pi_v$ is spherical. A spherical $\pi_v$ is a subquotient of $I(\chi_{\alpha_1}, \dots, \chi_{\alpha_n})$ for some $\alpha_i$, and then $\{\alpha_1, \dots, \alpha_n\}$ is a Satake parameter of $\pi$ at $v$. The Satake parameter at $v$ is unique.
6. (Irreducibility.) If $\alpha_i \ne N(w)\,\alpha_j$ for all $i, j$, then every subquotient of $I(\chi_{\alpha_1}, \dots, \chi_{\alpha_n})$ on $\mathrm{GL}_n(M_w)$ is spherical. This holds because the principal series is then irreducible (Bernstein and Zelevinsky).

*Proof.* By fact 5, $\pi_v$ is spherical and is a subquotient of $I(\chi_{\alpha_1}, \dots, \chi_{\alpha_n})$ with $\{\alpha_i\}$ a Satake parameter at $v$. By uniqueness, $B = \{\alpha_1, \dots, \alpha_n\}$. Facts 2, 3 and 4 show that $\Pi_w$ is a subquotient of $I(\chi_{\alpha_1} \circ \mathrm{N}, \dots, \chi_{\alpha_n} \circ \mathrm{N})$. Since $w$ is totally ramified, $\mathrm{N}$ maps a uniformizer of $M_w$ to a uniformizer of $K_v$ times a unit, and it maps units to units. So $\chi_{\alpha_i} \circ \mathrm{N}$ is the unramified character of $M_w^\times$ with value $\alpha_i$ at a uniformizer.

Next, $\alpha_i \ne N(v)\,\alpha_j$ for all $i, j$. Indeed, after a twist by a unitary character (which keeps the ratio $\alpha_i/\alpha_j$ and is unramified at $v$), the [Jacquet-Shalika bound](/entry/jacquet-shalika-bound/) gives $N(v)^{-1/2} < |\alpha_i| < N(v)^{1/2}$ for all $i$. Then $|\alpha_i| / |\alpha_j| < N(v)$, so $\alpha_i = N(v)\alpha_j$ is impossible. Since $N(w) = N(v)$, fact 6 shows that $\Pi_w$ is spherical, and fact 5 for $\Pi$ at $w$ shows that $\{\alpha_1, \dots, \alpha_n\} = B$ is a Satake parameter of $\Pi$ at $w$. $\square$

**Remark 7.18.3.** The hypothesis on $B$ is essential: the theorem says nothing at a ramified place where $\pi$ itself is ramified. The proof uses the weak base change hypothesis only through fact 3 and fact 4, where it is an assumption of the local theorem.

**Remark 7.18.4 (Formalization).** The theorem is the one-line term [QuadLift.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalIdeles/QuadLift.lean#L10): `ramSphOf` applied to `locGal` and to `liftGood`, itself fed with `coreId`, `varEx`, `varTrace` and `elemPairJ_holds`. The same file derives `quadLift` from it (line 14). The proof `ramSphOf` is at [RamSphOf.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalIdeles/RamSphOf.lean#L51); fact 1 is `normRam` together with a private lemma, fact 3 is `weakStable`, fact 5 is `satDict` with `SSatUniq_holds`, fact 6 is `unlSph`, and the Jacquet-Shalika step is `unlinked`. The statement `SatDict` allows the Satake parameter to be $\{\alpha_i^{\varepsilon}\}$ with $\varepsilon = \pm 1$; it is proved with $\varepsilon = 1$, and `ramSphOf` handles both signs, so the branch $\varepsilon = -1$ is never used. The part of `LocGal` that identifies $\mathrm{N}$ with the field norm is dropped in the proof. We did not unfold the predicate `IsLocGal` that describes $\sigma_w$.
