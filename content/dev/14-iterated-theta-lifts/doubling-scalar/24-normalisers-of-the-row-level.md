---
title: Normalisers of the row level
decls:
  - GlobalTheory.LevNorm.frame_normaliser
  - GlobalTheory.LevNorm.inst_normaliser
  - GlobalTheory.LevNorm.setting_normaliser
  - GlobalTheory.LevNorm.matches_differ
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Normalisers of the row level

The row of the open orbit chapter has a level group $K_2$ in the finite adelic unitary group, with a character $\chi_2$. Its reduction at a set of type places is a symmetric unipotent group, and $\chi_2$ is a generic character of it. This section finds the elements that normalise $K_2$ and fix $\chi_2$. Up to the centre and $K_2$, they are the elements of the finite Bessel group that commute with that group. As a result, two translates that match the row level differ by a central element of the anisotropic group. This last fact is used in [the central difference of matching translates](/entry/matches-differ-central-alt/) of the open orbit chapter.

**Setting.** Let $E/F$ be a CM extension with conjugation $\sigma$, and let $\widehat{\mathcal{O}}$ be the integral finite adeles of $E$. An *instance* $I$ is a hermitian space $E^n$ with Gram matrix $J$, a lattice $L$, and the finite adelic unitary group $G_f$. For $n = 2\rho + \kappa + 1$, let $\mathrm{U}_{\mathrm{sym}}(k)$ be the symmetric unipotent subgroup of $\mathrm{GL}_n(k)$ over a field $k$, with the set of symmetric edges $(i, j)$ of $(\rho, \kappa)$. For a matrix $a$ over $k$, the *edge value* of $M$ is $\sum a_{ij} M_{ij}$ over the symmetric edges. For a scalar $c$, let $\delta(c)$ be the diagonal matrix with $c$ at the indices $\rho \leq i < \rho + \kappa$ and $1$ at the others. We write $x \equiv M \bmod N$ when all entries of $x - M$ are divisible by $N$ in $\widehat{\mathcal{O}}$.

**Theorem 2.24.1 (Normaliser in a frame).** Let $g \neq 1$ be a natural number, and let $n = 2\rho + \kappa + 1$ with $\rho \geq 1$ and $\kappa \geq 2$. Let $\beta \in \mathrm{GL}_n(\mathbb{A}_{E,f})$ be a frame of $L$. Let $P_g$ be a finite set of places of $E$ that divide $g$, such that no place of $P_g$ is conjugate to a place of $P_g$, and such that for each self conjugate place $Q$ there is an integral $\delta$ with $\delta - \sigma\delta \not\equiv 0 \bmod Q$. For $Q \in P_g$, let $\psi_Q$ be a nontrivial additive character of the residue field $k_Q$, and let $a_Q$ be a matrix over $k_Q$ with nonzero entries at the symmetric edges. Let $K \subset G_f$ and $\chi \colon G_f \to \mathbb{C}$ be such that $x \in K$ exactly when $x$ stabilises the lattice of $\beta$ and the reduction of $\beta^{-1} x \beta$ at each $Q \in P_g$ lies in $\mathrm{U}_{\mathrm{sym}}(k_Q)$, and such that on $K$
$$\chi(x) = \prod_{Q \in P_g} \psi_Q\big(\text{edge value of } a_Q \text{ at the reduction of } \beta^{-1} x \beta\big).$$
Let $y \in G_f$ normalise $K$ and fix $\chi$. Then there are a central $z \in G_f$ and an integral $c$ with $c\, \sigma(c) = 1$ and $c \equiv 1 \bmod N$ for every $N$ prime to $g$, such that: for every $d \in G_f$ and every integral $x$ with $\beta x \beta^{-1} = d$ and $x \equiv \delta(c) \bmod g$, we have $d^{-1} z^{-1} y \in K$.

Lean: `GlobalTheory.LevNorm.frame_normaliser`.

*Proof.* Write $m = \beta^{-1} y \beta$.

1. *Gram matrix of the frame.* Let $G = \bar\beta^{t} J \beta$. Then $w$ is unitary for $G$ exactly when $\beta w \beta^{-1}$ is unitary for $J$.
2. *The level is kept.* Since $y$ and $y^{-1}$ normalise $K$ and fix $\chi$, both $m$ and $m^{-1}$ map integral matrices with symmetric unipotent reductions at $P_g$ to such matrices, and keep the edge characters.
3. *Normaliser core.* By the core theorem on normalisers of symmetric levels, $m = z\, x_1$ with $z$ a scalar adele, $z \sigma(z) = 1$, $x_1$ integral, and $c$ integral with $c \sigma(c) = 1$. Also $(1 - c) b$ is integral for every $b$ that is integral at $P_g$ together with $\sigma b$, and the reduction of $x_1$ at each $Q \in P_g$ is $\delta(c) h_Q$ with $h_Q \in \mathrm{U}_{\mathrm{sym}}(k_Q)$.
4. *Centre.* The scalar $z$ is unitary and commutes with every element, so it is central in $G_f$.
5. *Congruence of $c$.* Let $N$ be prime to $g$. Each place of $P_g$ divides $g$, so $N$ is a unit there. Then $b = 1/N$ is integral at $P_g$, and so is $\sigma b$. By step 3, $(1 - c)/N$ is integral.
6. *Conclusion.* Let $d$ and $x$ be as stated. Then $d^{-1} z^{-1} y = \beta\, x^{-1} x_1\, \beta^{-1}$, which stabilises the lattice. At $Q \in P_g$, $g = 0$ in $k_Q$, so $x$ reduces to $\delta(c)$, and $x^{-1} x_1$ reduces to $\delta(c)^{-1} \delta(c) h_Q = h_Q$. So $d^{-1} z^{-1} y \in K$. $\square$

**Theorem 2.24.2 (Normaliser of an instance).** Let $D$ be a tower datum with $r_S \geq 1$, let $I$ be its instance, and let $g = g_0 g_1$ be the product of its two type primes. Let $(e_0, f_0, z_0, b, b')$ be a reference frame of $I$ for $g$. Let $\psi_f$ be an additive character of $\mathbb{A}_{E,f}$, trivial on $\widehat{\mathcal{O}}$, with $\psi_f(x) \psi_\infty(x) = 1$ for $x \in E$. Let $K_2$ and $\chi_2$ be the level and character of the reference frame. Let $y \in G_f$ normalise $K_2$ and fix $\overline{\chi_2}$. Then there is a frame $\beta$ that lifts the flag vectors of the reference frame, with the conclusion of the last theorem for $K = K_2$ and $\rho = r_S$.

Lean: `GlobalTheory.LevNorm.inst_normaliser`.

*Proof.* We bring $K_2$ into the form of the last theorem.

1. *Type places.* Choose a set $P_g$ of type places. By the theorem on type places, no two of them are conjugate. Choose a nontrivial additive character $\psi_Q$ of each residue field.
2. *Ranks.* Since $m$ is even with $m \geq 2$ and $m + 3 \leq \kappa$, $n = 2 r_S + \kappa + 1$ with $\kappa \geq 2$. Also $g \neq 0$ and $g \neq 1$, since $g_0$ and $g_1$ are prime.
3. *Lifting frame.* The flag vectors are integral and span modulo $g$. By the lifting theorem there is a frame $\beta$ of $L$ that lifts them.
4. *Residues.* The product of the type primes is squarefree at every type place. So an integral adele is $0 \bmod g$ when its residues and those of its conjugate vanish at $P_g$.
5. *The character.* The character $s \mapsto \overline{\psi_f(s/g)}$ on $\widehat{\mathcal{O}}$ is trivial on $g \widehat{\mathcal{O}}$, by step 4. By the theorem on characters of residue fields, it is a product of generic shifts of the $\psi_Q$. Its support condition uses integral adeles with prescribed residues and the nontrivial values of $\psi_f$ at each prime.
6. *Reading in the frame.* By reading $K_2$ in $\beta$, there are matrices $a_Q$ with nonzero symmetric edges such that $K_2$ and $\overline{\chi_2}$ have the form of the last theorem.
7. *Conclusion.* Apply the last theorem. Its condition on conjugate places comes from step 1, and the condition on self conjugate places from the integers $\delta$ with $\delta - \bar\delta \notin Q$. $\square$

**Theorem 2.24.3 (Normaliser of the setting).** Let $X$ be a Hida setting whose instance is that of $D$, with $r_S \geq 1$. Let $u$ be a word, $H_f(u)$ the finite Bessel group of $u$ and $x_u$ the translate of $u$. Let $y \in G_f$ normalise $K_2$ and fix $\overline{\chi_2}$. Then there are a central $z$, an element $w \in H_f(u)$ that commutes with every element of $H_f(u)$, and $k \in K_2$, with
$$y = x_u^{-1}\, w\, x_u\, z\, k.$$

Lean: `GlobalTheory.LevNorm.setting_normaliser`.

*Proof.* The last theorem gives $\beta$, $z$ and $c$. By the theorem on the scalar complement of the frame, there are $w \in H_f(u)$ that commutes with $H_f(u)$ and an integral $x$ with $\beta x \beta^{-1} = x_u^{-1} w x_u$ and $x \equiv \delta(c) \bmod g$. Let $d = x_u^{-1} w x_u$. Then $k = d^{-1} z^{-1} y \in K_2$. Since $z$ is central, $y = d z k$. $\square$

**Theorem 2.24.4 (Matching translates differ by the centre).** Let $X$ be as above, $u$ a word, $\psi$ an additive character and $A$ a hermitian space. Let $B$ be a Bessel datum: a decomposition of $Y_0$ with anisotropic part $V_0 = A \oplus L$, and an embedding $\mathrm{emb}_A$ of the group of $A$ into that of $Y_0$ whose image is $H_\infty(u) \times H_f(u)$. Let $J$ be a set and $\chi$ a function on the group of $Y_0$. Say that $t$ *matches* if $t$ has trivial infinite part and conjugation by $t$ carries $(J, \chi)$ to the row level and its character. If $t$ and $t'$ match, there are $z$ central with trivial infinite part, $a$ central in the group of $A$ with trivial infinite part, and $k \in J$, with
$$t = \tilde x_u^{-1}\, \mathrm{emb}_A(a)\, \tilde x_u\, z\, t'\, k,$$
where $\tilde x_u$ is $x_u$ placed in the finite component.

Lean: `GlobalTheory.LevNorm.matches_differ`.

*Proof.* Let $j$ place an element of $G_f$ in the finite component.

1. Since $t$ and $t'$ have trivial infinite parts, $t t'^{-1} = j(y)$ for some $y$.
2. Both match, so $y$ normalises $K_2$ and fixes $\overline{\chi_2}$.
3. The last theorem gives $z$, $w$ and $k$ with $y = x_u^{-1} w x_u z k$.
4. As $w \in H_f(u)$, $j(w) = \mathrm{emb}_A(a)$ for some $a$, and $a$ has trivial infinite part. Since $w$ commutes with $H_f(u)$ and $\mathrm{emb}_A$ is injective, $a$ is central. Also $j(z)$ is central.
5. The element $t'^{-1} j(k) t'$ lies in $J$, since $t'$ matches. Then $t = j(y)\, t'$ has the stated form. $\square$

**Remark 2.24.5 (Formalization).** The four theorems are in [SettingNormaliser.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SettingNormaliser.lean#L43), at lines 43, 186 and 250, and in [MatchingTranslatesBottom.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/MatchingTranslatesBottom.lean#L39). The core theorem of step 3 is in [NormaliserCore.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/NormaliserCore.lean#L157), and matching and Bessel data are in [ThetaIdentityOfMapsAll.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/ThetaIdentityOfMapsAll.lean#L72). The congruence of $c$ is stated for every $N$ prime to $g$, which includes $N = 0$ only if $g = 1$; the hypothesis $g \neq 1$ excludes this. The next result in the same file, the central difference theorem (line 80), takes a hypothesis on the bottom of the tower and the membership of $t$ and $t'$ in a set, and uses neither (line 81). We have read the statements, not the proofs, of the core theorem, the lifting, residue and character theorems of the instance, and the scalar complement theorem.
